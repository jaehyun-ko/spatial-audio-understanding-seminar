"""Continuous scientific introduction, slides 02–07. Independently authored ManimCE."""
from __future__ import annotations
import json
import os
from pathlib import Path
import numpy as np
from manim import *

DRAFT = os.environ.get('INTRO_DRAFT') == '1'
config.pixel_width = 1136 if DRAFT else 2272
config.pixel_height = 404 if DRAFT else 808
config.frame_width = 14.2
config.frame_height = 5.05
config.frame_rate = 15 if DRAFT else 60
config.background_color = '#F6F8FA'
BG, INK, MUTED = '#F6F8FA', '#142233', '#586879'
C1, C2, EXTRA = '#008B9A', '#1F5FAE', '#A95018'
GRID, RULE = '#DCE4ED', '#A9B8C8'
ROOT = Path(__file__).resolve().parents[2]
C = 343.0

def mt(s, size=32, color=INK):
    return MathTex(s, font_size=size, color=color)

def txt(s, size=27, color=INK):
    return Text(s, font='Pretendard', font_size=size, color=color)

def curve(points, color=INK, width=3):
    m = VMobject(stroke_color=color, stroke_width=width)
    m.set_points_as_corners(np.asarray(points))
    return m

def spherical(r, alpha, beta):
    return r*np.array([np.cos(beta)*np.cos(alpha), np.cos(beta)*np.sin(alpha), np.sin(beta)])

def reflect(source, mic, wall=3.8):
    image = source.copy(); image[1] = 2*wall-source[1]
    u = (wall-mic[1])/(image[1]-mic[1])
    point = mic + u*(image-mic)
    return point, np.linalg.norm(image-mic)

def pulse(t):
    # Time is milliseconds. Arbitrary amplitude; a compact nonperiodic example signal.
    return np.exp(-(t/1.55)**2)*(np.cos(2*np.pi*0.46*t)+0.28*np.sin(2*np.pi*0.79*t))

class SpatialAudioIntro(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.alpha = ValueTracker(45*DEGREES)
        self.beta = ValueTracker(25*DEGREES)
        self.r = ValueTracker(3.8)
        self.d = ValueTracker(1.2)
        self.reflection = ValueTracker(0)
        self.other = ValueTracker(0)
        self.reveal = ValueTracker(28)
        self.labels = []
        self.checkpoints = []
        self.build_world()
        self.next_section('s02')
        self.stage_coordinates()
        self.finish('s02')
        self.next_section('s03')
        self.stage_observations()
        self.finish('s03')
        self.next_section('s04')
        self.stage_delay()
        self.finish('s04')
        self.next_section('s05')
        self.stage_mixture()
        self.finish('s05')
        self.next_section('s06')
        self.stage_array()
        self.finish('s06')
        self.next_section('s07')
        self.stage_scope()
        self.finish('s07')
        out = ROOT/'tmp/intro-sequence'
        out.mkdir(parents=True, exist_ok=True)
        (out/('checkpoints-draft.json' if DRAFT else 'checkpoints.json')).write_text(json.dumps(self.checkpoints, ensure_ascii=False, indent=2))

    def p(self):
        return spherical(self.r.get_value(), self.alpha.get_value(), self.beta.get_value())

    def mic(self, idx):
        return np.array([(-1 if idx == 0 else 1)*self.d.get_value()/2, 0., 0.])

    def project(self, p):
        # A fixed oblique scientific drawing; all acoustic calculations use 3D p, never screen distances.
        x,y,z = np.asarray(p)
        return np.array([-3.25+0.85*(x-0.52*y), -1.35+0.85*(0.38*y+0.90*z), 0.])

    def lab(self, m):
        self.labels.append(m)
        return m

    def finish(self, name):
        self.wait(1.25)
        self.checkpoints.append(dict(section=name, time=float(self.time), source=self.p().tolist(), spacing=self.d.get_value(), delay_ms=self.delay(), labels=[dict(text=getattr(m,'tex_string',getattr(m,'text','')), center=m.get_center().tolist(), width=float(m.width), height=float(m.height)) for m in self.labels if m in self.get_mobject_family_members()]))

    def build_world(self):
        P = self.project
        self.floor = VGroup()
        for x in [-2,-1,0,1,2,3]:
            self.floor.add(Line(P([x,-0.6,0]),P([x,3.8,0]),color=GRID,stroke_width=0.9))
        for y in [0,1,2,3]:
            self.floor.add(Line(P([-2.2,y,0]),P([3.6,y,0]),color=GRID,stroke_width=0.9))
        self.axes = VGroup(*[Arrow(P(a),P(b),buff=0,color=MUTED,stroke_width=2,tip_length=0.12,max_tip_length_to_length_ratio=0.08) for a,b in [([-2.2,0,0],[3.7,0,0]),([0,-0.6,0],[0,4.0,0]),([0,0,0],[0,0,3.45])]])
        self.axis_labels = VGroup(
            self.lab(mt('x',27,MUTED).move_to(P([3.9,0,0]))),
            self.lab(mt('y',27,MUTED).move_to(P([0,4.0,0])+np.array([-0.19,0.15,0]))),
            self.lab(mt('z',27,MUTED).move_to(P([0,0,3.6]))),
            self.lab(mt('O',26,MUTED).move_to(P([0,0,0])+np.array([-.14,.22,0]))))
        self.origin = Dot(P([0,0,0]), radius=0.04,color=INK)
        self.mics = VGroup()
        self.mic_labels = VGroup()
        for i,col in enumerate([C1,C2]):
            # Microphone acoustic center is precisely on the x axis, stem is a pictogram.
            mic = VGroup(Circle(radius=0.12,color=col,stroke_width=2.5).set_fill(BG,1), Line([0,-0.12,0],[0,-0.27,0],color=col,stroke_width=2),Line([-.12,-.27,0],[.12,-.27,0],color=col,stroke_width=2))
            mic.add_updater(lambda m,i=i:m.shift(P(self.mic(i))-m[0].get_center()))
            label=self.lab(mt(rf'M_{i+1}',29,col))
            label.add_updater(lambda m,i=i:m.move_to(P(self.mic(i))+np.array([-.10 if i==0 else .10,-.44,0])))
            self.mics.add(mic); self.mic_labels.add(label)
        self.source = VGroup(Dot(radius=.095,color=INK), Arc(radius=.20,start_angle=-.65,angle=1.3,color=INK,stroke_width=2),Arc(radius=.30,start_angle=-.65,angle=1.3,color=INK,stroke_width=2))
        self.source.add_updater(lambda m:m.shift(P(self.p())-m[0].get_center()))
        self.source_label=self.lab(mt(r's(t)',31))
        self.source_label.add_updater(lambda m:m.move_to(P(self.p())+np.array([0,.40,0])))
        self.source_name=self.lab(txt('음원',27))
        self.source_name.add_updater(lambda m:m.move_to(P(self.p())+np.array([.67,.04,0])))
        self.radius_line=always_redraw(lambda:Line(P([0,0,0]),P(self.p()),color=C2,stroke_width=3))
        self.radius_label=self.lab(mt('r',33,C2))
        self.radius_label.add_updater(lambda m:m.move_to(P(.62*self.p())+np.array([-.22,.05,0])))
        self.projection=always_redraw(lambda:VGroup(DashedLine(P(self.p()),P(self.p()*[1,1,0]),color=MUTED,dash_length=.055,stroke_width=1.5),DashedLine(P([0,0,0]),P(self.p()*[1,1,0]),color=MUTED,dash_length=.055,stroke_width=1.5),Dot(P(self.p()*[1,1,0]),radius=.04,color=C2)))
        self.azimuth=always_redraw(lambda:curve([P([1.12*np.cos(a),1.12*np.sin(a),0]) for a in np.linspace(0,self.alpha.get_value(),60)],C2,3))
        self.elevation=always_redraw(lambda:curve([P(spherical(1.54,self.alpha.get_value(),b)) for b in np.linspace(0,self.beta.get_value(),50)],C1,3))
        self.az_label=self.lab(mt(r'\alpha',31,C2))
        self.az_label.add_updater(lambda m:m.move_to(P(spherical(1.37,.5*self.alpha.get_value(),0))+np.array([.16,.17,0])))
        self.el_label=self.lab(mt(r'\beta',31,C1))
        self.el_label.add_updater(lambda m:m.move_to(P(spherical(1.78,self.alpha.get_value(),.5*self.beta.get_value()))+np.array([.16,.06,0])))

    def stage_coordinates(self):
        self.play(FadeIn(self.floor),Create(self.axes),FadeIn(self.axis_labels,self.origin),run_time=1.3)
        self.play(FadeIn(self.mics,self.mic_labels),FadeIn(self.source,self.source_label,self.source_name),run_time=1)
        self.coord_rows=VGroup()
        row_specs=[(r'\alpha','방위각','azimuth',C2,1.15),(r'\beta','고도각','elevation',C1,0),(r'r','거리','distance',C2,-1.15)]
        for symbol,ko,en,col,y in row_specs:
            sym=self.lab(mt(symbol,53,col).move_to([1.35,y,0]))
            name=self.lab(txt(ko,34).move_to([2.75,y+.05,0]))
            eng=self.lab(txt(en,24,MUTED).move_to([4.45,y+.03,0]))
            self.coord_rows.add(VGroup(sym,name,eng))
        self.play(FadeIn(self.projection),run_time=.65)
        self.play(Create(self.azimuth),FadeIn(self.az_label,self.coord_rows[0]),run_time=1.25)
        self.wait(.45)
        self.play(Create(self.elevation),FadeIn(self.el_label,self.coord_rows[1]),run_time=1.25)
        self.wait(.45)
        self.play(Create(self.radius_line),FadeIn(self.radius_label,self.coord_rows[2]),run_time=1.25)
        self.goal_geometry=VGroup(self.projection,self.azimuth,self.elevation,self.az_label,self.el_label,self.radius_line,self.radius_label)
        self.wait(.6)

    def length(self,i): return np.linalg.norm(self.p()-self.mic(i))
    def arrival(self,i): return 1000*self.length(i)/C
    def delay(self): return self.arrival(1)-self.arrival(0)

    def plot_point(self,t,a,row):
        return np.array([.85+5.8*t/28, (.65 if row==0 else -.65)+.38*a, 0.])

    def signal(self,t,i):
        direct=(3.8/self.length(i))*pulse(t-self.arrival(i))
        _,length=reflect(self.p(),self.mic(i))
        reflection=.62*(3.8/length)*pulse(t-1000*length/C)
        q=np.array([-2.15,1.15,.7])
        qlength=np.linalg.norm(q-self.mic(i))
        other=.40*(3.8/qlength)*pulse((t-6-1000*qlength/C)*.76)
        return direct+self.reflection.get_value()*reflection+self.other.get_value()*other

    def waveform(self,i):
        t=np.linspace(0,max(.01,self.reveal.get_value()),380)
        amps=self.signal(t,i)
        points=np.column_stack([.85+5.8*t/28, (.65 if i==0 else -.65)+.38*amps,np.zeros(len(t))])
        return curve(points,[C1,C2][i],3.5)

    def build_plots(self):
        self.plot_axes=VGroup()
        for i,col in enumerate([C1,C2]):
            self.plot_axes.add(Line(self.plot_point(0,0,i),self.plot_point(28,0,i),color=RULE,stroke_width=1.2))
            self.plot_axes.add(Line(self.plot_point(0,-1.4,i),self.plot_point(0,1.4,i),color=RULE,stroke_width=1.2))
            label=self.lab(mt(rf'x_{i+1}(t)',30,col).move_to([.15,.65 if i==0 else -.65,0]))
            self.plot_axes.add(label)
        for t in [0,8,16,24]:
            xp=self.plot_point(t,0,1)[0]
            self.plot_axes.add(Line([xp,-1.24,0],[xp,-1.31,0],color=RULE,stroke_width=1))
            self.plot_axes.add(self.lab(mt(str(t),23,MUTED).move_to([xp,-1.47,0])))
        self.time_label=self.lab(mt(r't\;(\mathrm{ms})',25,MUTED).move_to([6.22,-1.79,0]))
        self.plot_axes.add(self.time_label)
        self.waves=VGroup(*[always_redraw(lambda i=i:self.waveform(i)) for i in [0,1]])

    def stage_observations(self):
        self.play(FadeOut(self.coord_rows),FadeOut(self.goal_geometry),FadeOut(self.source_name),run_time=1.2)
        self.paths=VGroup(*[always_redraw(lambda i=i:Line(self.project(self.p()),self.project(self.mic(i)),color=[C1,C2][i],stroke_width=3)) for i in [0,1]])
        self.path_labels=VGroup()
        for i,col in enumerate([C1,C2]):
            m=self.lab(mt(rf'\ell_{i+1}',30,col))
            m.add_updater(lambda m,i=i:m.move_to(self.project(.5*(self.p()+self.mic(i)))+np.array([-.42 if i==0 else .26,.05,0])))
            self.path_labels.add(m)
        self.play(Create(self.paths),FadeIn(self.path_labels),run_time=1.1)
        self.build_plots()
        self.reveal.set_value(0)
        self.play(FadeIn(self.plot_axes),run_time=.75)
        self.add(self.waves)
        propagation=ValueTracker(0)
        dots=VGroup(*[always_redraw(lambda i=i:Dot(self.project(self.p()+min(propagation.get_value()/self.length(i),1)*(self.mic(i)-self.p())),radius=.066,color=[C1,C2][i])) for i in [0,1]])
        self.add(dots)
        self.play(propagation.animate.set_value(C*.028),self.reveal.animate.set_value(28),run_time=4.2,rate_func=linear)
        self.play(FadeOut(dots),run_time=.4)
        self.observation_eq=self.lab(mt(r'x_m(t)=a_m\,s(t-t_m)',34).move_to([3.7,1.8,0]))
        self.play(FadeIn(self.observation_eq),run_time=.8)

    def build_delay_marks(self):
        def marks():
            x1=self.plot_point(self.arrival(0),0,0)[0]
            x2=self.plot_point(self.arrival(1),0,0)[0]
            return VGroup(
                DashedLine([x1,-1.15,0],[x1,1.2,0],color=C1,stroke_width=1.5,dash_length=.06),
                DashedLine([x2,-1.15,0],[x2,1.2,0],color=C2,stroke_width=1.5,dash_length=.06),
                Line([min(x1,x2),.0,0],[max(x1,x2)+.0001,.0,0],color=INK,stroke_width=2.2),
                Line([x1,-.08,0],[x1,.08,0],color=INK,stroke_width=2),
                Line([x2,-.08,0],[x2,.08,0],color=INK,stroke_width=2))
        self.delay_marks=always_redraw(marks)
        self.t_labels=VGroup()
        for i,col in enumerate([C1,C2]):
            label=self.lab(mt(rf't_{i+1}',24,col))
            label.add_updater(lambda m,i=i:m.move_to([self.plot_point(self.arrival(i),0,i)[0],1.32 if i==0 else -1.11,0]))
            self.t_labels.add(label)
        self.delay_number=DecimalNumber(self.delay(),num_decimal_places=2,include_sign=True,font_size=34,color=INK)
        self.delay_number.add_updater(lambda m:m.set_value(self.delay()).move_to([4.0,-2.08,0]))
        self.delay_readout=VGroup(self.lab(mt(r'\tau=',35).move_to([2.82,-2.08,0])),self.delay_number,self.lab(mt(r'\mathrm{ms}',28,MUTED).move_to([4.97,-2.08,0])))

    def stage_delay(self):
        self.delay_eq=self.lab(mt(r'\tau=t_2-t_1=\frac{\ell_2-\ell_1}{c}',37).move_to([3.65,1.89,0]))
        self.play(TransformMatchingTex(self.observation_eq,self.delay_eq),run_time=1)
        self.build_delay_marks()
        self.play(FadeIn(self.delay_marks,self.t_labels,self.delay_readout),run_time=.75)
        self.play(self.alpha.animate.set_value(110*DEGREES),run_time=3.3,rate_func=smooth)
        self.wait(.7)
        self.play(self.alpha.animate.set_value(45*DEGREES),run_time=3.3,rate_func=smooth)
        self.wait(.6)

    def stage_mixture(self):
        self.mixture_eq=self.lab(mt(r'x_m(t)=\sum_k(h_{mk}*s_k)(t)+v_m(t)',33).move_to([3.7,1.85,0]))
        self.play(TransformMatchingTex(self.delay_eq,self.mixture_eq),FadeOut(self.delay_marks,self.t_labels,self.delay_readout),run_time=1.1)
        P=self.project
        self.wall=Polygon(*[P(p) for p in [[-2.2,3.8,0],[3.6,3.8,0],[3.6,3.8,3.0],[-2.2,3.8,3.0]]],fill_color=GRID,fill_opacity=.3,stroke_color=RULE,stroke_width=1.3)
        self.reflections=VGroup()
        for i,col in enumerate([C1,C2]):
            point,_=reflect(self.p(),self.mic(i))
            self.reflections.add(DashedLine(P(self.p()),P(point),color=col,stroke_width=2,dash_length=.07),DashedLine(P(point),P(self.mic(i)),color=col,stroke_width=2,dash_length=.07),Dot(P(point),radius=.038,color=col))
        self.wall_label=self.lab(txt('1차 반사',26,MUTED).move_to([-5.55,1.9,0]))
        self.wall.set_z_index(-2)
        self.add(self.wall);self.bring_to_back(self.wall)
        self.play(FadeIn(self.wall,self.wall_label),Create(self.reflections),self.reflection.animate.set_value(1),run_time=2.7)
        self.wait(.75)
        q=np.array([-2.15,1.15,.7]);qp=P(q)
        self.other_source=Dot(qp,radius=.09,color=EXTRA)
        self.other_label=self.lab(mt(r's_2(t)',29,EXTRA).move_to(qp+np.array([-.3,-.28,0])))
        self.other_paths=VGroup(*[DashedLine(qp,P(self.mic(i)),color=EXTRA,stroke_width=2,dash_length=.08) for i in [0,1]])
        new_source_label=self.lab(mt(r's_1(t)',31))
        new_source_label.add_updater(lambda m:m.move_to(P(self.p())+np.array([0,.40,0])))
        self.play(FadeIn(self.other_source,self.other_label),Create(self.other_paths),TransformMatchingTex(self.source_label,new_source_label),run_time=1.2)
        self.source_label=new_source_label
        self.play(self.other.animate.set_value(1),run_time=2.2)
        self.mixture_key=VGroup(VGroup(Line(LEFT*.22,RIGHT*.22,color=MUTED,stroke_width=2),self.lab(txt('직접음',23,MUTED))).arrange(RIGHT,buff=.12),VGroup(DashedLine(LEFT*.22,RIGHT*.22,color=MUTED,stroke_width=2,dash_length=.08),self.lab(txt('반사음',23,MUTED))).arrange(RIGHT,buff=.12),VGroup(Dot(radius=.045,color=EXTRA),self.lab(txt('다른 음원',23,EXTRA))).arrange(RIGHT,buff=.12)).arrange(RIGHT,buff=.28).move_to([3.6,-2.12,0])
        self.play(FadeIn(self.mixture_key),run_time=.8)
        self.wait(.6)

    def stage_array(self):
        original_source_label=self.lab(mt(r's(t)',31))
        original_source_label.add_updater(lambda m:m.move_to(self.project(self.p())+np.array([0,.40,0])))
        self.array_eq=self.lab(mt(r'\tau=\frac{\|\mathbf p_s-\mathbf p_2\|-\|\mathbf p_s-\mathbf p_1\|}{c}',31).move_to([3.7,1.86,0]))
        self.play(FadeOut(self.wall,self.wall_label,self.reflections,self.other_source,self.other_label,self.other_paths,self.mixture_key),self.reflection.animate.set_value(0),self.other.animate.set_value(0),TransformMatchingTex(self.mixture_eq,self.array_eq),TransformMatchingTex(self.source_label,original_source_label),run_time=1.5)
        self.source_label=original_source_label
        self.d_bracket=always_redraw(lambda:VGroup(Line(self.project(self.mic(0))+[0,-.72,0],self.project(self.mic(1))+[0,-.72,0],color=INK,stroke_width=1.8),*[Line(self.project(self.mic(i))+[0,-.66,0],self.project(self.mic(i))+[0,-.78,0],color=INK,stroke_width=1.8) for i in [0,1]]))
        self.d_label=self.lab(mt('d',31).move_to(self.project([0,0,0])+[0,-.98,0]))
        self.array_condition=self.lab(txt('음원 위치·좌표계 고정',25,MUTED).move_to([-3.65,1.92,0]))
        self.play(FadeIn(self.d_bracket,self.d_label,self.array_condition,self.delay_marks,self.delay_readout,self.t_labels),run_time=.7)
        self.play(self.d.animate.set_value(.6),run_time=2)
        self.wait(.45)
        self.play(self.d.animate.set_value(1.8),run_time=3)
        self.wait(.45)
        self.play(self.d.animate.set_value(1.2),run_time=1.4)

    def stage_scope(self):
        self.play(FadeOut(self.array_eq,self.array_condition,self.delay_marks,self.delay_readout,self.t_labels,self.d_bracket,self.d_label,self.waves,self.plot_axes,self.paths,self.path_labels),FadeIn(self.goal_geometry),FadeIn(self.source_name),run_time=1.4)
        # Reading perspectives, not a fabricated single-model architecture.
        rows=VGroup()
        for y,title,detail,symbol,color in [
            (1.2,'공간 표현',r'(\hat\alpha,\hat\beta,\hat r)',r'\hat{\mathbf p}_s',C2),
            (0,'언어 결합',r'\{\mathrm{class},\alpha,\beta,r\}',r's_k',C1),
            (-1.2,'평가',r'\Delta x\;\longleftrightarrow\;\Delta\hat y',r'\Delta',EXTRA)]:
            name=self.lab(txt(title,29,color).move_to([1.55,y+.20,0]))
            expression=self.lab(mt(detail,34).move_to([4.65,y+.12,0]))
            line=Line([.55,y-.40,0],[6.65,y-.40,0],color=GRID,stroke_width=1)
            rows.add(VGroup(name,expression,line))
        self.scope_rows=rows
        for row in rows:
            self.play(FadeIn(row,shift=UP*.08),run_time=.85)
            self.wait(.65)
        self.wait(.7)
