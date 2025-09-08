
import os
import cv2
import numpy as np
from PIL import Image

def display(image):
    """Helper function to display an image for debugging."""
    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def error(prv, cur):
    """Calculates the mean squared error between two images."""
    prv = np.array(prv, dtype=np.float64) / 255.0
    cur = np.array(cur, dtype=np.float64) / 255.0
    return np.sum((prv - cur) ** 2)

def images_to_pdf_a4(image_paths, output_pdf_path):
    """
    Arranges images vertically, creating new pages when content overflows A4 size.
    """
    A4_WIDTH, A4_HEIGHT = 2480, 3508  # A4 size in pixels at 300 DPI
    MARGIN = 100  # Margin in pixels

    if not image_paths:
        print("No images to generate PDF.")
        return

    pages = []
    current_height = MARGIN
    current_page = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), 'white')

    for image_path in image_paths:
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Scale image to fit the page width while maintaining aspect ratio
        target_width = A4_WIDTH - 2 * MARGIN
        if img_width != target_width:
            scale_factor = target_width / img_width
            img = img.resize((int(img_width * scale_factor), int(img_height * scale_factor)), Image.LANCZOS)
            img_width, img_height = img.size

        # If image overflows, save current page and create a new one
        if current_height + img_height > A4_HEIGHT - MARGIN:
            pages.append(current_page)
            current_page = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), 'white')
            current_height = MARGIN

        # Paste image onto the current page
        paste_position = (MARGIN, current_height)
        current_page.paste(img, paste_position)
        current_height += img_height

    pages.append(current_page)

    # Save all pages to a single PDF
    pages[0].save(output_pdf_path, save_all=True, append_images=pages[1:])

def make_pdf(main_directory):
    """
    Filters unique tab images and compiles them into a single PDF.
    Images are first scaled to a standard width before being compared for uniqueness.
    """
    directory = os.path.join(main_directory, "tabs")
    output_pdf_path = os.path.join(main_directory, 'output.pdf')

    imp_files = sorted([os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))])

    if not imp_files:
        print("No image files found in the 'tabs' directory.")
        return

    A4_WIDTH, _ = 2480, 3508
    MARGIN = 100
    TARGET_WIDTH = A4_WIDTH - 2 * MARGIN
    
    # This threshold is higher because we are comparing larger, scaled images.
    # It may require tuning for different video styles.
    THRESHOLD = 2000.0
    
    use_files = []
    prv_scaled_img = None

    for image_path in imp_files:
        cur_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if cur_img is None:
            continue

        # Scale current image to the target width for a consistent comparison
        h, w = cur_img.shape
        scale_factor = TARGET_WIDTH / w
        new_h = int(h * scale_factor)
        cur_scaled_img = cv2.resize(cur_img, (TARGET_WIDTH, new_h), interpolation=cv2.INTER_AREA)

        if prv_scaled_img is None:
            # Always include the first image
            use_files.append(image_path)
            prv_scaled_img = cur_scaled_img
            continue

        # Pad the shorter image to match the height of the taller one for comparison
        h1, w1 = prv_scaled_img.shape
        h2, w2 = cur_scaled_img.shape
        max_h = max(h1, h2)
        
        comp1 = np.full((max_h, TARGET_WIDTH), 255, dtype=np.uint8)
        comp2 = np.full((max_h, TARGET_WIDTH), 255, dtype=np.uint8)
        
        comp1[0:h1, 0:w1] = prv_scaled_img
        comp2[0:h2, 0:w2] = cur_scaled_img

        if error(comp1, comp2) > THRESHOLD:
            use_files.append(image_path)

        prv_scaled_img = cur_scaled_img

    images_to_pdf_a4(use_files, output_pdf_path)
    print(f"Output is at {output_pdf_path}")
