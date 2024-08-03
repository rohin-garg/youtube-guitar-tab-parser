import os
import cv2
import yt_dlp

def download_youtube_video(url, output_path):
    ydl_opts = {
        'format': 'best[ext=mp4]',  # This will select the best quality single mp4 file
        'outtmpl': os.path.join(output_path, 'video.%(ext)s')
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return os.path.join(output_path, f"video.{info['ext']}")

def extract_frames(video_path, output_folder, interval=2):
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")

    fps = video.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        raise ValueError("FPS value is zero, unable to extract frames.")
    frame_interval = int(fps * interval)
    print(f"FPS: {fps}, Frame Interval: {frame_interval}")

    success, frame = video.read()
    count = 0
    frame_count = 0

    while success:
        if count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            frame_count += 1
        success, frame = video.read()
        count += 1

    video.release()
    print(f"Extracted {frame_count} frames.")

def download(main_directory):
    youtube_url = input("Enter the YouTube video URL: ")
    output_folder = main_directory

    video_path = download_youtube_video(youtube_url, output_folder)
    print(f"Video downloaded: {video_path}")

    frames_folder = os.path.join(output_folder, "frames")
    extract_frames(video_path, frames_folder)
    print(f"Frames extracted to: {frames_folder}")
