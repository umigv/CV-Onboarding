Here you will use what you learned in the previous module to create and run your own script for the model. Work on the yolo_cp.py file and commit your finished version to your branch of the repo. If you get stuck consider using the hints provided below.
[This link](https://docs.ultralytics.com/modes/predict/#streaming-source-for-loop) will also help you through. You should have two video streams running, one as an occupancy grid black and white and the other with a live segmentation mask over the original video.

<details>
<summary>Hint 1</summary>
Use cap.get with the argument of the cv2.desired_attribute and case it as an int
</details>

<details>
<summary>Hint 2</summary>
Use the cv2.fillPoly function
</details>
