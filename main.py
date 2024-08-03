from clear_files import clear_all
from download_frames import download
from extract_tab_pics import extract_tab
from clean_tab import make_pdf

main_directory = 'C:/Users/rohin/Desktop/projects/guitar_tab/frames'
clear_all(main_directory)
download(main_directory)
extract_tab(main_directory)
make_pdf(main_directory)
