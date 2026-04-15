from manim import *
import os, json

class OwnScene(Scene):
    def __init__(self):
        super().__init__()
        self.segments = []

    def segment(self, name):
        self.wait(0.01)
        t = self.renderer.time
        t = round(t, 3)
        print(f"[SEGMENT] {name} at {t:.2f}s")
        self.segments.append({"name": name, "time": t})

    def save_segments(self):
        import os
        import json

        # This ALWAYS works across versions
        video_path = self.renderer.file_writer.movie_file_path
        output_dir = os.path.dirname(video_path)

        path = os.path.join(output_dir, "segments.json")

        with open(path, "w") as f:
            json.dump(self.segments, f, indent=2)

        print(f"\nSaved segments to: {path}\n")

class MainScene(OwnScene):
    def construct(self):
        self.segment("First_Point")
        circle = Circle(2, BLUE)
        self.play(Create(circle), run_time = 2)
        self.wait(1)

        self.segment("Second_Point")
        self.play(FadeOut(circle))
        self.wait(2)

        self.save_segments()
