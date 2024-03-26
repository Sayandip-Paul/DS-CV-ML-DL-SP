import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from ultralytics import YOLO

# Load YOLO model
model = YOLO(r'D:\Vehicle_Detection_YoloV8\colab_run\best.pt')

# Create tkinter GUI
root = tk.Tk()
root.title("YOLO Object Detection")


# Function to open a file dialog to select an image
def open_image():
    file_path = filedialog.askopenfilename()
    return file_path


# Function to process image with YOLO and display the results
def process_image():
    image_path = open_image()
    if image_path:
        results = model(image_path)  # Run inference on the image
        result = results[0]  # We assume only one image is processed

        # Save the result image
        result.save(filename='result.jpg')

        # Convert the result image to a format suitable for displaying in Tkinter
        img_pil = Image.open('result.jpg')
        img_pil = img_pil.resize((400, 300))  # Resize for display purposes
        img_tk = ImageTk.PhotoImage(img_pil)

        # Display the image in the Tkinter window
        label_image.config(image=img_tk)
        label_image.image = img_tk


# Button to upload image and process it
upload_button = tk.Button(root, text="Upload Image", command=process_image)
upload_button.pack()

# Label to display processed image
label_image = tk.Label(root)
label_image.pack()

root.mainloop()
