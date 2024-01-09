import moviepy.editor as mp

clip = mp.VideoFileClip("NEW INVENTIONS THAT WILL BLOW YOUR MIND.mp4")
duration = clip.duration
start_time = 0
end_time = 60

while end_time < duration:
    clip_resized = clip.subclip(start_time, end_time)
    clip_resized.write_videofile(f"movie_{start_time}_{end_time}.mp4")
    start_time += 60
    end_time += 60

if end_time >= duration:
    clip_resized = clip.subclip(start_time, duration)
    clip_resized.write_videofile(f"movie_{start_time}_{duration}.mp4")
