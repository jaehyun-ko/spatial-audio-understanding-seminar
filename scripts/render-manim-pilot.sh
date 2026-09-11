#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
venv_python="$project_root/.venv/bin/python"
venv_manim="$project_root/.venv/bin/manim"
media_root="$project_root/tmp/manim-media"
rendered_video="$media_root/videos/tdoa_ipd_wrap/606p30/tdoa-ipd-wrap.mp4"
public_dir="$project_root/public/animations"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required to create the isolated Manim environment." >&2
  exit 1
fi

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg is required to prepare the web video and poster." >&2
  exit 1
fi

if [[ ! -x "$venv_python" ]]; then
  uv venv --python 3.12 "$project_root/.venv"
fi

uv pip install --python "$venv_python" -r "$project_root/manim/requirements.txt"

"$venv_manim" \
  -c "$project_root/manim/manim.cfg" \
  --media_dir "$media_root" \
  -v WARNING \
  "$project_root/manim/tdoa_ipd_wrap.py" \
  TDoAToIPDWrap \
  -o tdoa-ipd-wrap.mp4

mkdir -p "$public_dir"
ffmpeg -y -loglevel error \
  -i "$rendered_video" \
  -c copy -movflags +faststart \
  "$public_dir/tdoa-ipd-wrap.mp4"
ffmpeg -y -loglevel error \
  -i "$public_dir/tdoa-ipd-wrap.mp4" \
  -an -c:v libvpx-vp9 -crf 32 -b:v 0 -pix_fmt yuv420p \
  "$public_dir/tdoa-ipd-wrap.webm"
ffmpeg -y -loglevel error \
  -ss 0.70 -i "$public_dir/tdoa-ipd-wrap.mp4" \
  -frames:v 1 \
  "$public_dir/tdoa-ipd-wrap-start.png"
ffmpeg -y -loglevel error \
  -sseof -0.35 -i "$public_dir/tdoa-ipd-wrap.mp4" \
  -frames:v 1 \
  "$public_dir/tdoa-ipd-wrap-poster.png"

echo "Rendered public/animations/tdoa-ipd-wrap.mp4"
echo "Rendered public/animations/tdoa-ipd-wrap.webm"
echo "Rendered public/animations/tdoa-ipd-wrap-start.png"
echo "Rendered public/animations/tdoa-ipd-wrap-poster.png"
