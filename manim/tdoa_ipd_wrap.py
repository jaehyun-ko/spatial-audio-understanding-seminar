from __future__ import annotations

import numpy as np
from manim import (
    AnimationGroup,
    Arc,
    Arrow,
    Circle,
    Create,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    Flash,
    GrowFromCenter,
    LaggedStart,
    Line,
    MathTex,
    PI,
    Scene,
    Transform,
    TransformFromCopy,
    TransformMatchingTex,
    VGroup,
    VMobject,
    ValueTracker,
    always_redraw,
    config,
    linear,
    smooth,
)


# The animation fills the 1136 × 404 body frame of the Slidev seminar layout.
config.pixel_width = 1704
config.pixel_height = 606
config.frame_width = 14.22
config.frame_height = 5.05
config.frame_rate = 30
config.background_color = "#F6F8FA"

# Match the light seminar theme, including the rendered video and its poster.
BG = "#F6F8FA"
INK = "#142233"
MUTED = "#586879"
SIGNAL = "#008B9A"
GEOMETRY = "#1F5FAE"
FOCUS = "#1F5FAE"
NEGATIVE = "#A95018"
RULE = "#8495A5"


def formula(*parts: str, size: int = 36, color: str = INK) -> MathTex:
    return MathTex(*parts, font_size=size, color=color)


def microphone(color: str) -> VGroup:
    head = Circle(radius=0.15, stroke_color=color, stroke_width=3)
    head.set_fill(color, opacity=0.16)
    stem = Line([0, -0.15, 0], [0, -0.35, 0], color=color, stroke_width=3)
    base = Line([-0.16, -0.35, 0], [0.16, -0.35, 0], color=color, stroke_width=3)
    return VGroup(head, stem, base)


def source_icon() -> VGroup:
    core = Dot(radius=0.1, color=FOCUS)
    waves = VGroup(
        *[
            Arc(
                radius=radius,
                start_angle=-0.9,
                angle=1.8,
                color=FOCUS,
                stroke_width=3,
            )
            for radius in (0.25, 0.42, 0.59)
        ]
    )
    return VGroup(core, waves)


def polyline(points: list[np.ndarray], color: str, width: float = 5) -> VMobject:
    curve = VMobject(stroke_color=color, stroke_width=width)
    curve.set_points_as_corners(points)
    return curve


class TDoAToIPDWrap(Scene):
    """A silent, low-density explanation of delay becoming wrapped phase."""

    def construct(self) -> None:
        self.camera.background_color = BG
        self.stage_path_to_delay()
        self.stage_delay_to_wrapped_phase()

    def stage_path_to_delay(self) -> None:
        source = source_icon().move_to([-5.45, 1.05, 0])

        mic1 = microphone(SIGNAL).move_to([-1.65, -0.58, 0])
        mic2 = microphone(GEOMETRY).move_to([1.95, -0.58, 0])
        mic1_name = formula(r"M_1", size=25, color=SIGNAL).next_to(mic1, np.array([0, -1, 0]), buff=0.08)
        mic2_name = formula(r"M_2", size=25, color=GEOMETRY).next_to(mic2, np.array([0, -1, 0]), buff=0.08)

        path1 = Line(source[0].get_center(), mic1[0].get_center(), color=SIGNAL, stroke_width=4)
        path2 = Line(source[0].get_center(), mic2[0].get_center(), color=GEOMETRY, stroke_width=4)
        path1.set_opacity(0.82)
        path2.set_opacity(0.82)
        path1_name = formula(r"\ell_1", size=26, color=SIGNAL)
        path2_name = formula(r"\ell_2", size=26, color=GEOMETRY)
        path1_name.move_to(path1.point_from_proportion(0.50) + np.array([0, 0.24, 0]))
        path2_name.move_to(path2.point_from_proportion(0.59) + np.array([0, 0.24, 0]))

        delta_eq = formula(r"\Delta\ell", "=", r"\ell_2", "-", r"\ell_1", size=42)
        delta_eq[0].set_color(FOCUS)
        delta_eq[2].set_color(GEOMETRY)
        delta_eq[4].set_color(SIGNAL)
        delta_eq.move_to([4.65, 0.48, 0])

        tau_eq = formula(r"\tau", "=", r"\frac{\Delta\ell}{c}", size=44)
        tau_eq[0].set_color(SIGNAL)
        tau_eq.set_color_by_tex(r"\Delta\ell", FOCUS)
        tau_eq.move_to([4.65, -0.62, 0])

        self.play(
            LaggedStart(
                GrowFromCenter(source),
                GrowFromCenter(mic1),
                GrowFromCenter(mic2),
                FadeIn(mic1_name, mic2_name),
                lag_ratio=0.12,
            ),
            run_time=0.7,
        )
        self.play(
            Create(path1),
            Create(path2),
            FadeIn(path1_name, path2_name),
            run_time=0.7,
        )

        travelled = ValueTracker(0)
        length1 = path1.get_length()
        length2 = path2.get_length()
        pulse1 = always_redraw(
            lambda: Dot(
                path1.point_from_proportion(min(travelled.get_value() / length1, 1)),
                radius=0.075,
                color=SIGNAL,
            )
        )
        pulse2 = always_redraw(
            lambda: Dot(
                path2.point_from_proportion(min(travelled.get_value() / length2, 1)),
                radius=0.075,
                color=GEOMETRY,
            )
        )
        self.add(pulse1, pulse2)
        self.play(travelled.animate.set_value(length1), run_time=1.05, rate_func=linear)
        self.play(
            Flash(mic1[0].get_center(), color=SIGNAL, flash_radius=0.34, line_length=0.12),
            run_time=0.28,
        )
        self.play(travelled.animate.set_value(length2), run_time=0.72, rate_func=linear)
        self.play(
            Flash(mic2[0].get_center(), color=GEOMETRY, flash_radius=0.34, line_length=0.12),
            FadeOut(pulse1, pulse2),
            FadeIn(delta_eq, shift=np.array([0, 0.08, 0])),
            run_time=0.38,
        )
        self.play(
            TransformMatchingTex(
                delta_eq.copy(),
                tau_eq,
                transform_mismatches=True,
                path_arc=-PI / 4,
            ),
            run_time=0.72,
        )
        self.wait(0.25)

        self.mic_pair = VGroup(mic1, mic2, mic1_name, mic2_name)
        self.geometry = VGroup(source, path1, path2, path1_name, path2_name, delta_eq)
        self.tau_eq = tau_eq

    def stage_delay_to_wrapped_phase(self) -> None:
        compact_pair = self.mic_pair.copy().scale(0.54).move_to([-4.82, 1.02, 0])
        for mic, label in zip(compact_pair[:2], compact_pair[2:]):
            label.font_size = 22
            label.next_to(mic, np.array([0, -1, 0]), buff=0.08)
        tau_numeric = formula(r"\tau", "=", r"0.5\,\mathrm{ms}", size=35)
        tau_numeric[0].set_color(SIGNAL)
        tau_numeric.move_to([-4.82, 1.86, 0])

        self.play(
            Transform(self.mic_pair, compact_pair),
            TransformMatchingTex(self.tau_eq, tau_numeric, transform_mismatches=True),
            FadeOut(self.geometry),
            run_time=0.78,
            rate_func=smooth,
        )

        phase_center = np.array([-4.82, -0.56, 0])
        phase_radius = 0.88
        phase_circle = Circle(radius=phase_radius, color=RULE, stroke_width=3).move_to(phase_center)
        phase_zero_tick = Line(
            phase_center + np.array([phase_radius - 0.08, 0, 0]),
            phase_center + np.array([phase_radius + 0.08, 0, 0]),
            color=MUTED,
            stroke_width=2,
        )
        phase_pi_tick = Line(
            phase_center - np.array([phase_radius - 0.08, 0, 0]),
            phase_center - np.array([phase_radius + 0.08, 0, 0]),
            color=NEGATIVE,
            stroke_width=2,
        )
        phase_labels = VGroup(
            formula("0", size=24, color=MUTED).next_to(phase_zero_tick, np.array([1, 0, 0]), buff=0.07),
            formula(r"\pm\pi", size=24, color=NEGATIVE).next_to(phase_pi_tick, np.array([-1, 0, 0]), buff=0.07),
            formula(r"\Delta\phi", size=25, color=FOCUS).next_to(phase_circle, np.array([0, -1, 0]), buff=0.16),
        )

        left, right = -2.35, 6.48
        bottom, top = -1.52, 1.35

        def graph_point(freq_khz: float, phase: float) -> np.ndarray:
            x = left + (right - left) * freq_khz / 4.2
            y = bottom + (top - bottom) * (phase + PI) / (2 * PI)
            return np.array([x, y, 0])

        x_axis = Line(graph_point(0, 0), graph_point(4.2, 0), color=RULE, stroke_width=2)
        y_axis = Line(graph_point(0, -PI), graph_point(0, PI), color=RULE, stroke_width=2)
        top_rule = DashedLine(
            graph_point(0, PI),
            graph_point(4.2, PI),
            color=NEGATIVE,
            stroke_width=2,
            dash_length=0.08,
        )
        bottom_rule = DashedLine(
            graph_point(0, -PI),
            graph_point(4.2, -PI),
            color=NEGATIVE,
            stroke_width=2,
            dash_length=0.08,
        )
        bounds = VGroup(
            formula(r"+\pi", size=24, color=NEGATIVE).next_to(top_rule, np.array([-1, 0, 0]), buff=0.08),
            formula(r"-\pi", size=24, color=NEGATIVE).next_to(bottom_rule, np.array([-1, 0, 0]), buff=0.08),
            formula(r"\Delta\phi", size=25, color=MUTED).next_to(y_axis, np.array([0, 1, 0]), buff=0.08),
        )

        ticks = VGroup()
        for value in range(1, 5):
            point = graph_point(value, 0)
            tick = Line(
                point + np.array([0, -0.07, 0]),
                point + np.array([0, 0.07, 0]),
                color=RULE,
                stroke_width=2,
            )
            number = formula(str(value), size=24, color=MUTED)
            number.move_to(graph_point(value, -PI) + np.array([0, -0.19, 0]))
            ticks.add(tick, number)
        x_name = formula(r"f\;(\mathrm{kHz})", size=25, color=MUTED)
        x_name.move_to([right - 0.42, bottom - 0.43, 0])

        phase_eq = formula(
            r"\Delta\phi", "=", r"\operatorname{wrap}\!\left(2\pi f", r"\tau", r"\right)", size=36
        )
        phase_eq[0].set_color(FOCUS)
        phase_eq[3].set_color(SIGNAL)
        phase_eq.move_to([(left + right) / 2, 1.92, 0])

        self.play(
            AnimationGroup(
                Create(phase_circle),
                Create(phase_zero_tick),
                Create(phase_pi_tick),
                lag_ratio=0.08,
            ),
            FadeIn(phase_labels),
            AnimationGroup(
                Create(x_axis),
                Create(y_axis),
                Create(top_rule),
                Create(bottom_rule),
                lag_ratio=0.06,
            ),
            FadeIn(bounds, ticks, x_name),
            run_time=0.72,
        )
        self.play(
            FadeIn(VGroup(*phase_eq[:3], phase_eq[4]), shift=np.array([0, 0.08, 0])),
            TransformFromCopy(tau_numeric[0], phase_eq[3]),
            run_time=0.52,
        )

        frequency = ValueTracker(0.03)

        def unwrapped_phase(freq_khz: float) -> float:
            return PI * freq_khz

        def wrapped_phase(freq_khz: float) -> float:
            return ((unwrapped_phase(freq_khz) + PI) % (2 * PI)) - PI

        def phase_endpoint() -> np.ndarray:
            angle = unwrapped_phase(frequency.get_value())
            return phase_center + phase_radius * np.array([np.cos(angle), np.sin(angle), 0])

        phase_vector = Arrow(
            phase_center,
            phase_endpoint(),
            buff=0,
            color=FOCUS,
            stroke_width=5,
            tip_length=0.16,
        )
        phase_vector.add_updater(lambda mob: mob.put_start_and_end_on(phase_center, phase_endpoint()))
        phase_dot = Dot(phase_endpoint(), radius=0.07, color=FOCUS)
        phase_dot.add_updater(lambda mob: mob.move_to(phase_endpoint()))
        phase_arc = always_redraw(
            lambda: Arc(
                radius=0.46,
                start_angle=0,
                angle=wrapped_phase(frequency.get_value()),
                arc_center=phase_center,
                color=SIGNAL,
                stroke_width=3,
            )
        )

        graph_dot = Dot(
            graph_point(frequency.get_value(), wrapped_phase(frequency.get_value())),
            radius=0.08,
            color=FOCUS,
        )
        graph_dot.add_updater(
            lambda mob: mob.move_to(graph_point(frequency.get_value(), wrapped_phase(frequency.get_value())))
        )
        guide = DashedLine(
            graph_point(frequency.get_value(), -PI),
            graph_point(frequency.get_value(), wrapped_phase(frequency.get_value())),
            color=FOCUS,
            stroke_width=2,
            dash_length=0.07,
        )
        guide.add_updater(
            lambda mob: mob.put_start_and_end_on(
                graph_point(frequency.get_value(), -PI),
                graph_point(frequency.get_value(), wrapped_phase(frequency.get_value())),
            )
        )

        def phase(freq_khz: float, turns: int) -> float:
            return PI * freq_khz - 2 * PI * turns

        segment_specs = ((0.03, 0.98, 0), (1.02, 2.98, 1), (3.02, 4.0, 2))
        segments = VGroup(
            *[
                polyline(
                    [
                        graph_point(value, phase(value, turns))
                        for value in np.linspace(start, end, 100)
                    ],
                    SIGNAL,
                )
                for start, end, turns in segment_specs
            ]
        )

        self.add(phase_arc, phase_vector, phase_dot, guide, graph_dot)
        self.play(
            FadeIn(phase_arc, phase_vector, phase_dot, guide, graph_dot),
            run_time=0.3,
        )
        self.play(
            frequency.animate.set_value(0.98),
            Create(segments[0]),
            run_time=1.08,
            rate_func=linear,
        )
        self.play(
            frequency.animate.set_value(1.02),
            Flash(graph_point(1, PI), color=NEGATIVE, flash_radius=0.25, line_length=0.08),
            Flash(graph_point(1, -PI), color=NEGATIVE, flash_radius=0.25, line_length=0.08),
            run_time=0.22,
            rate_func=linear,
        )
        self.play(
            frequency.animate.set_value(2.98),
            Create(segments[1]),
            run_time=1.32,
            rate_func=linear,
        )
        self.play(
            frequency.animate.set_value(3.02),
            Flash(graph_point(3, PI), color=NEGATIVE, flash_radius=0.25, line_length=0.08),
            Flash(graph_point(3, -PI), color=NEGATIVE, flash_radius=0.25, line_length=0.08),
            run_time=0.22,
            rate_func=linear,
        )
        self.play(
            frequency.animate.set_value(4.0),
            Create(segments[2]),
            run_time=0.72,
            rate_func=linear,
        )
        self.wait(1.2)
