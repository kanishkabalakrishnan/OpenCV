Face Detection Using OpenCV
This repository contains code for detecting faces in images and videos using OpenCV's Haar Cascade Classifier. The project includes three main functionalities:

1. Face Detection in Single and Multi-Face Images
Functionality:
   Detects faces in both single and multi-face images.
Usage:
  The code reads an image file and converts it to grayscale.
  It then detects faces using a pre-trained Haar Cascade model.
  Detected faces are highlighted with rectangles on the original image.
  Both the color image and grayscale image with detected faces are displayed.

3. Face Detection in Video Files
Functionality:
   Detects faces in video files.
Usage:
   The code opens a video file and processes it frame by frame.
   Each frame is converted to grayscale, and faces are detected and highlighted with rectangles.
   The processed video frames with detected faces are displayed in a window.
4. Face Detection Using Webcam
Functionality:
      Real-time face detection using a webcam.

Usage:
The code captures video from the webcam and processes each frame.
Faces are detected and highlighted with rectangles in real-time.
The live video feed with detected faces is displayed in a window.
Press 'Q' or 'q' to exit the webcam capture.

Requirements:
     OpenCV library (cv2):
           Ensure you have OpenCV installed. You can install it using pip install opencv-python.
     Haar Cascade XML file (haarcascade_frontalface_default.xml): 
           This file is required for face detection. It should be located in the same directory as the scripts.


Setup and Execution
1.Place your image or video file in the project directory.
2.Update the file paths in the scripts accordingly.
3.Run the desired script to see face detection in action.
