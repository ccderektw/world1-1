import subprocess
index = 1
args = ["ffmpeg", "-f video4linux2", "-i /dev/video0", "-s 1280x720", " -c:v h264", "-b:v 8000k", "-t 00:00:10", f"a{index}.mp4"]
p = subprocess.Popen(args)
print(p.out)
