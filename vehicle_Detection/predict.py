from ultralytics import YOLO

# Load a model
model = YOLO(r'D:\Vehicle_Detection_data\colab_run\best.pt')

# Run batched inference on a list of images
results = model([r'D:\Vehicle_Detection_data\Data\Test\images\23.jpg', r'D:\Vehicle_Detection_data\Data\Test\images\24.jpg'])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename='result.jpg')  # save to disk
