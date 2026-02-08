# 🧩 rubiks-cube-color-detection- - Simple Color Detection for Rubik's Cube

[![Download](https://img.shields.io/badge/Download-GitHub%20Releases-blue.svg)](https://github.com/NIKFLIX0409/rubiks-cube-color-detection-/releases)

## 🚀 About the Project
This project uses Python and OpenCV to detect the colors of a Rubik’s Cube face from images or live camera input. It simplifies the process of color detection, making it accessible for everyone.

## 📋 Features
- Detects cube sticker colors using HSV color space.
- Supports both image-based input and webcam input.
- Represents each cube face as a 3×3 color matrix.
- Modular and straightforward to extend or customize.

## ⚙️ Technologies Used
- Python: A popular programming language that is easy to learn.
- OpenCV: A powerful library for computer vision tasks.
- NumPy: A library for numerical operations in Python.

## 🗺️ Project Workflow
1. Capture an image using a webcam or load a stored image.
2. Resize and preprocess the image for better accuracy.
3. Convert the image from BGR to HSV color space.
4. Divide the image into a 3×3 grid to identify each cube face.
5. Extract a small region of interest (ROI) from each grid cell.
6. Average HSV values to reduce noise and enhance detection.
7. Classify each cell color based on the average HSV values.
8. Store the detected colors as cube face data for easy viewing.

## 📥 Download & Install
To download and install the application, please visit [this page](https://github.com/NIKFLIX0409/rubiks-cube-color-detection-/releases) to download the latest version.

## 🛠️ How to Run
1. **Install dependencies:**
   Open your command line interface and enter:
   ```bash
   pip install -r requirements.txt
   ```
   
2. **Run the application:**
   To start the program, enter:
   ```bash
   python main.py
   python camera_capture.py
   ```
   
3. The program will now detect the cube colors. You can expect outputs similar to:
   ```
   ['yellow', 'green', 'white']
   ['blue', 'red', 'blue']
   ['orange', 'yellow', 'green']
   ```

## 🌟 Limitations
The accuracy of color detection depends on lighting conditions. Make sure to use this program in an environment with good lighting.

## 📞 Support
If you encounter issues, feel free to open an issue in the GitHub repository. Your feedback is crucial for improving the application.

## 📚 Additional Resources
- [Python Official Documentation](https://www.python.org/doc/)
- [OpenCV Documentation](https://opencv.org/documentation/)
- [NumPy Documentation](https://numpy.org/doc/)