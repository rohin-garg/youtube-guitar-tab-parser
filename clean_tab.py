import os
import cv2
import numpy as np
from collections import Counter
from PIL import Image

def display(image):
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def error(prv, cur):
    prv = np.array(prv) / 255.0
    cur = np.array(cur) / 255.0

    ans = 0
    for i in range(prv.shape[0]):
        for j in range(prv.shape[1]):
            ans += (prv[i][j] - cur[i][j]) ** 2
    return ans

def images_to_pdf(image_paths, output_pdf_path):
    image_list = [Image.open(image).convert('RGB') for image in image_paths]
    image_list[0].save(output_pdf_path, save_all=True, append_images=image_list[1:])

def make_pdf(main_directory):
    directory = main_directory + "/tabs"
    output_pdf_path = main_directory

    count = 0
    imp_files = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(directory, filename)
            imp_files.append(image_path)

    THRESHOLD = 500 
    use_files = [imp_files[0]]
    for i in range(1, len(imp_files)):
        prv = cv2.imread(imp_files[i-1])
        cur = cv2.imread(imp_files[i])
        prv = cv2.cvtColor(prv, cv2.COLOR_BGR2GRAY)
        cur = cv2.cvtColor(cur, cv2.COLOR_BGR2GRAY)
        if error(prv, cur) > THRESHOLD:
            # display(cv2.imread(imp_files[i]))
            use_files.append(imp_files[i])

    images_to_pdf(use_files, output_pdf_path + '/output.pdf')

# make_pdf()

