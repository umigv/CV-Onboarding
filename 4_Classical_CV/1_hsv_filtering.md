### 🎨 HSV Filtering

HSV (Hue, Saturation, Value) is often more robust than RGB for color detection, especially under varying lighting conditions.

```python
import cv2
import numpy as np

img = cv2.imread("cones.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_orange = np.array([5, 100, 100])
upper_orange = np.array([15, 255, 255])

mask = cv2.inRange(hsv, lower_orange, upper_orange)
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Filtered", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


🔗 [HSV inRange Example (docs)](https://docs.opencv.org/4.x/da/d97/tutorial_threshold_inRange.html)