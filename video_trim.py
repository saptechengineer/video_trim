from moviepy.editor import VideoFileClip
my_clip = VideoFileClip('traffic_input.mp4')
#new_clip = my_clip.subclip(2,7).rotate(90)
new_clip = my_clip.subclip(23,27)
new_clip.write_videofile("clip.mp4", codec = "libx264", fps=25)