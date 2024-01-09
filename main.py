from pytube import YouTube
import moviepy.editor as mp
import os
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        download_path = youtubeObject.download()
        clip = mp.VideoFileClip(download_path)
        duration = clip.duration
        start_time = 0
        end_time = 60

        while end_time < 240:
            clip_resized = clip.subclip(start_time, end_time)
            clip_resized.write_videofile(f"movie_{start_time}_{end_time}.mp4")
            start_time += 60
            end_time += 60

        if end_time >= duration:
            clip_resized = clip.subclip(start_time, duration)
            clip_resized.write_videofile(f"movie_{start_time}_{duration}.mp4")
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)