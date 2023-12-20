##Title: Rock Pong game media pipe function
 # Date: 11/20/2023
 # Author: Catherine Sarte, Jose Venecia
 # 
 # Program Description: This program is designed to act as a function for a Pong style game that implements
 #the media pipe library and open cv. This program is the fucntion that implements open cv and media pip for
 #human pose detection. It takes the frames of an image, detects the pose location and reports the coordinates back to
 #the user. The function also splits the screen to a specfic side given the side choice of either 1(left) or 2(right) to 
 #be used for the game when function is implemented. Use "q" to quit.
 ##


#Imports
import cv2
import mediapipe as mp
import numpy as np

# This function is called by main to convert the media pipe pose locations for x and y coordinates
def mediapipe_to_pixel_coords(normalized_x, normalized_y, frame_width, frame_height):
    pixel_x = int(normalized_x * frame_width)
    pixel_y = int(normalized_y * frame_height)

    #Return x and y corrdinates
    return pixel_x, pixel_y

# This is the main function of the program to analyze given video capture
def main():
    #Side varaible to be changed based on the side that you want to capture and analyze for the game
    side = 1

    # Begin camera capture
    cap = cv2.VideoCapture(0)

    ## Setup mediapipe instance
    with mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        # While the camera is running
        while cap.isOpened():

            # Get the current frame 
            ret, frame = cap.read()
            
            # Set varaibles to hold the inital width and height of the camera frame
            wid = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            hei = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            
            # Width to split the image fram with
            halfWid = wid/2

            # Check which side of the frame to analyze
            if(side == 1): # For left side
                # Set width to be from 0 to the half width mark
                frame = frame[0:360, 0:int(halfWid)]
            else: # For right side
                # Set the width from the half width point to the width of the frame
                frame = frame[0:360, int(halfWid):int(wid)]
            
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
        
            # Make detection
            results = pose.process(image)
        
            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark
                print(mediapipe_to_pixel_coords(landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].y, wid, hei))
                print(mediapipe_to_pixel_coords(landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].y, wid, hei))
                print(mediapipe_to_pixel_coords(landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].y, wid, hei))
                print(mediapipe_to_pixel_coords(landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].y, wid, hei))

                # Convert elbow corrdinates to string
                left_elbow_coordinates = str(mediapipe_to_pixel_coords(landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp.solutions.pose.PoseLandmark.LEFT_ELBOW.value].y, wid, hei))
                right_elbow_coordinates = str(mediapipe_to_pixel_coords(landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp.solutions.pose.PoseLandmark.RIGHT_ELBOW.value].y, wid, hei))
                left_wrist_coordinates = str(mediapipe_to_pixel_coords(landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp.solutions.pose.PoseLandmark.LEFT_WRIST.value].y, wid, hei))
                right_wrist_coordinates = str(mediapipe_to_pixel_coords(landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp.solutions.pose.PoseLandmark.RIGHT_WRIST.value].y, wid, hei))
                
                # Display the found elbow coordinates for left and right

                cv2.putText(image, left_elbow_coordinates, (15,12), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)

                cv2.putText(image, right_elbow_coordinates, (15,30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                
            except:
                print("There was an exception during pose detection. Make sure you are in frame.")
                pass

            # Render detections
            mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, 
                                    mp.solutions.pose.POSE_CONNECTIONS,
                                    mp.solutions.drawing_utils.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp.solutions.drawing_utils.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )               
            
            # Display pose detections to screen
            cv2.imshow('Mediapipe Feed', image)

            #!!!!TO ADD!!!!
            #This function while loop shoud also be the loop running the window for the game and pong ball functionalities
            #take left_elbow_coordinates/ left_wrist_coordinates and right_elbow_corrdinates/ right_wrist_corrdinates, get their range of 
            #contact corrdinates and compare to ball location
            # If the ball is out of bounds, opposing player gets a point and and ball resets
            # If the ball location is within the contact range perform the physics movement to opposite direction

            # Check if user wants to quit the program
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
       
    
    


if __name__ == "__main__":
    main()