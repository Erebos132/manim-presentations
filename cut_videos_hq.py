import json
import subprocess

VIDEO_FILE = "./media/videos/scenes/1080p60/MainScene.mp4"
SEGMENTS_FILE = "./media/videos/scenes/1080p60/segments.json"
dir = "./splitted"

with open(SEGMENTS_FILE) as f:
    segments = json.load(f)

for i in range(len(segments)):
    start = segments[i]["time"]
    name = segments[i]["name"]

    if i < len(segments) - 1:
        end = segments[i + 1]["time"]
    else:
        end = None  # last segment goes to end

    path = f"{dir}/{i:02d}_{name}.mp4"

    cmd = [
        "ffmpeg",
        "-y",
        "-ss", str(start),
    ]

    if end is not None:
        duration = end - start
        cmd += ["-t", str(duration)]

    cmd += [
        "-i", VIDEO_FILE,
        "-c", "copy",
        path
    ]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd)

print("\nDone splitting!")

