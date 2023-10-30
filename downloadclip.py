import os
import subprocess
from pytube import YouTube
import re

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if video:
            video.download(save_path)
            print(f"Downloaded: {yt.title}")
        else:
            print("No suitable video streams found.")
    except Exception as e:
        print(f"Error: {e}")

def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h*3600 + m*60 + s

def clip_video(input_path, output_path, start_time, end_time):
    try:
        cmd = [
            'ffmpeg', '-i', input_path, 
            '-ss', start_time, 
            '-to', end_time, 
            '-c', 'copy', output_path
        ]
        subprocess.run(cmd)
        print(f"Trimmed video saved as: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the directory to save the video: ")

    yt = YouTube(url)
    title = re.sub(r'[^\w\s-]', '', yt.title).strip()  # Remove special characters and trim whitespace
    input_path = f'{save_path}/{title}.mp4'
    output_path = f'{save_path}/trimmed_video.mp4'

    if not os.path.exists(input_path):
        download_video(url, save_path)

    start_time = input("Enter the start time (hh:mm:ss): ")
    end_time = input("Enter the end time (hh:mm:ss): ")
    
    clip_video(input_path, output_path, start_time, end_time)
