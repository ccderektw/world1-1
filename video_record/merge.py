from moviepy.editor import VideoFileClip, clips_array
clip1 = VideoFileClip("a1.mp4") # Optionally add a margin with .margin(10)
clip2 = VideoFileClip("a2.mp4")
clip3 = VideoFileClip("a1.mp4") # Optionally add a margin with .margin(10)
clip4 = VideoFileClip("a2.mp4")
final_clip = clips_array([[clip1, clip2],[clip3, clip4]])
final_clip.resize(width=640).write_videofile("my_split.mp4") # Resized
final_clip.write_videofile("my_split.mp4") # Width will be combined width

