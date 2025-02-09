import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  

from tkinter import filedialog, Label, Button, Frame
import cv2
from PIL import Image, ImageTk
from utils.image_processing import histogram_equalization, contrast_stretching, sharpen

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global img, img_tk
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        display_image(img)

def display_image(image):
    img_resized = cv2.resize(image, (400, 400))
    img_pil = Image.fromarray(img_resized)
    img_tk = ImageTk.PhotoImage(img_pil)
    img_label.config(image=img_tk)
    img_label.image = img_tk

class ImageEnhancementUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Enhancement Tool")
        self.root.geometry("600x600")

        frame = Frame(root)
        frame.pack()

        global img_label
        img_label = Label(frame)
        img_label.pack()

        btn_load = Button(root, text="Load Image", command=load_image)
        btn_load.pack()

        btn_hist_eq = Button(root, text="Histogram Equalization", command=lambda: display_image(histogram_equalization(img)))
        btn_hist_eq.pack()

        btn_contrast = Button(root, text="Contrast Stretching", command=lambda: display_image(contrast_stretching(img)))
        btn_contrast.pack()

        btn_sharpen = Button(root, text="Sharpen", command=lambda: display_image(sharpen(img)))
        btn_sharpen.pack()
