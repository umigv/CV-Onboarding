import cv2
from ultralytics import YOLO
import numpy as np

def video_inference():
    model = YOLO('path_to_model.pt')

    #TODO grab a video feed using cv2 to define cap. Use a video from the UMARV CV dropbox
    cap = None

    #TODO Get image height and width and assign to 2 variables
    #Look under video capture properties section -> https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
    #Use Hint #1 if you struggle to implement this
    image_width = None
    image_height = None

    #TODO Setup occupancy grid - create a numpy array of zeros with defined image width and height
    occupancy_grid = None

    while (cap.isOpened()):
      
        success, frame = cap.read()
        if success: 

            #TODO refer to YOLO docs to define results as a model -> (near bottom) https://docs.ultralytics.com/modes/predict/#streaming-source-for-loop 
            results = None

            if results[0].masks is not None:
                    if(len(results[0].masks.xy) != 0):
                        
                        annotated_frame = results[0].plot()    
                        segment = results[0].masks.xy[0] 

                        #TODO Transfer segment into a numpy array 
                        #*you will have to pass in a second argument for the datatype
                        #to ensure it is compatible for cv2, dtype=np.int32*
                        segment_array = None

                        #TODO Find cv2 function to create segmenation maskes, take note of required parameters
                        #Use Hint #2 if you cannot find the function
                       
                        
                        #TODO use cv2.imshow to display your occupancy grid and annotated frames (separately)
                        
                       
                       
                        if cv2.waitKey(1) & 0xFF == ord("q"):
                            break

video_inference()

