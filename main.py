import argparse
import os
from clear_files import clear_all
from download_frames import download
from extract_tab_pics import extract_tab
from clean_tab import make_pdf

def main():
    parser = argparse.ArgumentParser(description='YouTube Guitar Tab Parser')
    parser.add_argument('url', help='The YouTube URL to parse.')
    parser.add_argument('output_dir', nargs='?', default='output', help='The directory to save the output files.')
    args = parser.parse_args()

    main_directory = args.output_dir
    youtube_url = args.url

    if not os.path.exists(main_directory):
        os.makedirs(main_directory)

    clear_all(main_directory)
    download(main_directory, youtube_url)
    extract_tab(main_directory)
    make_pdf(main_directory)

if __name__ == '__main__':
    main()
