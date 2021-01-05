from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("output_file.mp4")

# getting only first 5 seconds
clip = clip.subclip(0, 20)

# loading audio file
audioclip = AudioFileClip("temp-audio.m4a").subclip(0, 20)

# adding audio to the video clip
videoclip = clip.set_audio(audioclip)

# showing video clip
videoclip.ipython_display()
