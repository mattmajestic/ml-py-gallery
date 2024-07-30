import cv2
import numpy as np
import os

def process_image(file_path, output_dir):
    # Load image
    img = cv2.imread(file_path)

    # Convert image to HSV for working with numpy
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define yellow range
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Mask the yellow regions
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    yellow_regions = cv2.bitwise_and(img, img, mask=mask)

    # Grayscale
    gray = cv2.cvtColor(yellow_regions, cv2.COLOR_BGR2GRAY)

    # Identify edges
    edges = cv2.Canny(gray, 50, 150)

    # Enhance edges
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    edges = cv2.erode(edges, kernel, iterations=1)

    # Determine card contours
    min_card_area = 1000
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    card_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_card_area]

    # Save each detected card
    for i, contour in enumerate(card_contours):
        x, y, w, h = cv2.boundingRect(contour)
        card = img[y:y+h, x:x+w]
        output_path = os.path.join(output_dir, f'card_{os.path.basename(file_path).split(".")[0]}_{i+1}.jpg')
        cv2.imwrite(output_path, card)

def process_images_in_folder(folder_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            file_path = os.path.join(folder_path, filename)
            process_image(file_path, output_dir)

# Example usage
input_folder = './img'
output_folder = './output'
process_images_in_folder(input_folder, output_folder)
