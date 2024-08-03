import os
import cv2
import numpy as np
from collections import Counter
from region_selector import prompt_coords

def extract_tab(main_directory):
    directory = main_directory + "/frames"
    count = 0
    imp_files = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(directory, filename)
            imp_files.append(image_path)

    all_bounds = []
    med_path = imp_files[len(imp_files) // 2]
    bounds = prompt_coords(med_path)

    print(bounds)
    for image_path in imp_files:
        if count > 0:
            image = cv2.imread(image_path)
            if image is None:
                continue
            image_section = image[bounds[0]:bounds[2], bounds[1]:bounds[3]]
            cv2.imwrite(main_directory + f"/tabs/tab{count:04d}.png", image_section);

        count += 1
