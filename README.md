# Rubik’s Cube Color Detection

## About the Project
This project uses Python and OpenCV to detect the colors of a Rubik’s Cube face from images or live camera input.

## Features
- Detects cube sticker colors using HSV color space
- Supports image-based input and webcam input
- Represents each cube face as a 3×3 color matrix
- Modular and easy to extend

## Technologies Used
- Python
- OpenCV
- NumPy

## Project Workflow
1. Capture an image using a webcam or load a stored image
2. Resize and preprocess the image
3. Convert the image from BGR to HSV color space
4. Divide the image into a 3×3 grid
5. Extract a small region (ROI) from each grid cell
6. Average HSV values to reduce noise
7. Classify each cell color
8. Store detected colors as cube face data

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
python main.py
python camera_capture.py
['yellow', 'green', 'white']
['blue', 'red', 'blue']
['orange', 'yellow', 'green']

Limitations

Accuracy depends on lighting conditions

Reflections and shadows can affect color detection

Screen images may introduce glare

Solver logic is not implemented in this version

Future Improvements

Automatic lighting calibration

Improved color classification techniques

Full Rubik’s Cube solver integration

Real-time visual overlay on detected cube faces

Purpose

This project was developed as an academic project to understand computer vision and image processing concepts.
