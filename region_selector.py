import cv2
import time

drawing = False 
ix, iy = -1, -1
ex, ey = -1, -1
done = False

def draw_rectangle(event, x, y, flags, param):
    global done, ix, iy, ex, ey, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        print(f"Upper left corner: ({ix}, {iy})")
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            ex, ey = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        done = True
        ex, ey = x, y
        print(f"Bottom right corner: ({ex}, {ey})")
        print(f"Rectangle coordinates: Upper left ({ix}, {iy}), Bottom right ({ex}, {ey})")

def prompt_coords(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unable to load.")
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle)
    while not done:
        temp_image = image.copy()  # Copy the original image
        if drawing:
            cv2.rectangle(temp_image, (ix, iy), (ex, ey), (0, 255, 0), 2)
        cv2.imshow('image', temp_image)
        if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key
            break

    cv2.destroyAllWindows()
    return (iy, ix, ey, ex)

