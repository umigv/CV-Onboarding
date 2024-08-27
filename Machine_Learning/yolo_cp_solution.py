import cv2
from ultralytics import YOLO
import numpy as np

def video_inference():
    model = YOLO('your_model_name.pt')

    #model = YOLO('LLOnly180ep.pt')
    #grab a video feed using cv2 to define cap
    cap = cv2.VideoCapture('video_name.media_format')
    
    #cap = cv2.VideoCapture('IMG_3812.mp4')

    #Get image height and width and assign to 2 variables
    image_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    image_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #Setup occupancy grid - create a numpy array of zeros with defined image width and height
    occupancy_grid = np.zeros((image_width, image_height))

    while (cap.isOpened()):
      
        success, frame = cap.read()
        if success: 
            #refer to YOLO docs to define results as a model link -> (near bottom)
            results = model(frame)

            if results[0].masks is not None:
                    if(len(results[0].masks.xy) != 0):
                        

                        annotated_frame = results[0].plot()

                        
                        segment = results[0].masks.xy[0] #provide this
                        #Transfer segment into a numpy array, *you will have to pass in a second argument
                        #for the datatype to ensure it is compatible for cv2, dtype=np.int32*
                        segment_array = np.array([segment], dtype=np.int32)
                        #Find cv2 function to create segmenation maskes, take note of required parameters
                        cv2.fillPoly(occupancy_grid, [segment_array], color=(255, 0, 0))
                       
                        
                        #use cv2.imshow to display your videos
                        cv2.imshow('Occupancy Grid', occupancy_grid)
                        cv2.imshow('Annotated Frame', annotated_frame)
                       
                       
                        if cv2.waitKey(1) & 0xFF == ord("q"):
                            break
                   
video_inference()

