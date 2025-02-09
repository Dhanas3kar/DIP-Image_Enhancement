import cv2
import numpy as np

def resize_image(img, width, height):
    return cv2.resize(img, (width, height))

def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def save_image(img, file_path):
    cv2.imwrite(file_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
