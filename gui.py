import tkinter as tk
from tkinter import filedialog
import cv2
from cartoonizer import cartoonize_image

def select_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.png;*.jpeg;*.bmp")]
    )
    if file_path:
        cartoonize_image(file_path)

# Create GUI window
root = tk.Tk()
root.title("Image Cartoonizer")
root.geometry("300x200")

# Create Button
btn = tk.Button(root, text="Select Image", command=select_image, font=("Arial", 12))
btn.pack(pady=20)

root.mainloop()
