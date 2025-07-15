import os
import cv2
import yt_dlp

def download_youtube_video(url, output_path):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]/best[ext=mp4]/bestvideo',
        'outtmpl': os.path.join(output_path, 'video.%(ext)s'),
        'postprocessors': [],
        'merge_output_format': 'mp4',
        'verbose': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info)
            return video_path
        except yt_dlp.utils.DownloadError as e:
            print(f"Download error: {e}")
            raise

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

def resize_images_in_directory(directory):
    max_height = 500
    max_width = 1000
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')):
            image = cv2.imread(file_path)
            if image is None:
                continue

            height, width = image.shape[:2]

            scale_factor = 1
            if height > max_height:
                scale_factor = min(scale_factor, max_height / height)
            if width > max_width:
                scale_factor = min(scale_factor, max_width / width)

            if scale_factor < 1:
                new_size = (int(width * scale_factor), int(height * scale_factor))
                resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
                cv2.imwrite(file_path, resized_image)

def download(main_directory, youtube_url):
    output_folder = main_directory

    try:
        video_path = download_youtube_video(youtube_url, output_folder)
        print(f"Video downloaded: {video_path}")

        frames_folder = os.path.join(output_folder, "frames")
        extract_frames(video_path, frames_folder)
        resize_images_in_directory(frames_folder)
        print(f"Frames extracted to: {frames_folder}")
    except Exception as e:
        print(f"Error occurred: {e}")

