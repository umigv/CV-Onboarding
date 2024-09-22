import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 
import cv2
import matplotlib
import math

def region_of_interest(image,vertices):
    mask = np.zeros_like(image)

    fill_color = 255 #image.shape[2], # of color channels, for example in RGB it is 3 (originally, before grayscale conversion)
    cv2.fillPoly(mask,vertices,fill_color)

    masked_image = cv2.bitwise_and(image,mask) #255 and pixel = pixel, 0 and pixel = 0
    return masked_image


def draw_lines(img, lines, color=[255, 0, 0], thickness=3):
    if lines is None:
        return
    line_img = np.zeros_like(img)
    img = np.copy(img)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)   
    #addWeighted gives blended look
    img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)    
    return img


#load image

base_image = mpimg.imread("lanes.jpg")


#find edges with Canny edge detection
#convert to grayscale as only image intensity needed, reduces noise
gray_image = cv2.cvtColor(base_image,cv2.COLOR_RGB2GRAY)
cannyed_image = cv2.Canny(gray_image,100,200)

#cut down to region of interest: img.shape = [height, width, color channels]

region_of_interest_vertices = [(0,base_image.shape[0]),(base_image.shape[1]/2,base_image.shape[0]/2),(base_image.shape[1],base_image.shape[0])]

cropped_image = region_of_interest(cannyed_image,np.array([region_of_interest_vertices],np.int32))

#generate lines for edges using Hough Transform
lines = cv2.HoughLinesP(
    cropped_image,
    rho=6,              #Distance resolution in pixels
    theta=np.pi / 60,  #Angle resolution in radians
    threshold=160,      #Min. number of intersecting points to detect a line  
    lines=np.array([]), #Vector to return start and end points of the lines indicated by [x1, y1, x2, y2] 
    minLineLength=40,   #Line segments shorter than this are rejected
    maxLineGap=25       #Max gap allowed between points on the same line
)

#lined_image = draw_lines(base_image,lines)

#distinguish the left and right lane lines independently and show each line individually - how? Slope
#Due to unique coordinate system, positive slope in normal coord system is negative here
#average lines into a single line that fits

left_line_x = []
left_line_y = []
right_line_x = []
right_line_y = []
for line in lines:
    for x1, y1, x2, y2 in line:
        slope = (y2 - y1) / (x2 - x1) # <-- Calculating the slope.
        if math.fabs(slope) < 0.5: # <-- Only consider extreme slope
            continue
        if slope <= 0: # <-- If the slope is negative, left group.
            left_line_x.extend([x1, x2])
            left_line_y.extend([y1, y2])
        else: # <-- Otherwise, right group.
            right_line_x.extend([x1, x2])
            right_line_y.extend([y1, y2])


min_y = int(base_image.shape[0] * (3 / 5)) # <-- Just below the horizon
max_y = int(base_image.shape[0]) # <-- The bottom of the image
poly_left = np.poly1d(np.polyfit(
    left_line_y,
    left_line_x,
    deg=1
))
left_x_start = int(poly_left(max_y))
left_x_end = int(poly_left(min_y))
poly_right = np.poly1d(np.polyfit(
    right_line_y,
    right_line_x,
    deg=1
))


right_x_start = int(poly_right(max_y))
right_x_end = int(poly_right(min_y))

line_image = draw_lines(base_image,[[[left_x_start, max_y, left_x_end, min_y],[right_x_start, max_y, right_x_end, min_y],]],thickness=5,)

plt.figure()
plt.imshow(line_image)
plt.show()
