# mediaPipe_PoseDetection_PongGame
Authors: Catherine Sarte, Jose Venecia

 Documentation Used:
 Renotte, N (2021) MediaPipePoseEstimation/MediaPipePoseTutorial. https://github.com/nicknochnack/MediaPipePoseEstimation.git

This repository holds the Python media pipe functionality to be able to split a video capture screen and collect/display the coordinate location of the left and right arm to be used in a rock climbing wall pong game

This function was developed in the fall of 2023 to eventually be applied to a rock-climbing pong-style game that is set to be completed in spring 2024. 

Running the program:
  1. install necessary libraries - cv2, mediapipe, numpy
  2. On line 33: cap = cv2.VideoCapture(0)
     - make sure to access your camera you also use 0. It is different for some systems
  4. run the program
  5. The program will open your camera and begin displaying coordinate detections
     - move around and watch the corrdinates change
  6. To change the side of the camera to detect the right side instead of the left:
      - change line 30 from (side = 1) to (side = 2) 
  8. Once you want to stop running the camera and program type "q"
