### ✏️ Drawing Contours
Contours help you detect and outline shapes in an image.

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
```
🔗 [Contour Detection Example (docs)](https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours.html)