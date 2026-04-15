set x 0

if test $x -eq 0
  manim -ql scenes.py MainScene
  python ./cut_videos_lq.py
end

if test $x -eq 1
  manim -qh scenes.py MainScene
  python ./cut_videos_hq.py
end
