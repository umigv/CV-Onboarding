### 🌀 Perspective Transforms
Used to perform a bird's-eye (top-down) view transformation or rectify skewed images.
```python
pts1 = np.float32([[100,100],[200,100],[100,200],[200,200]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (300,300))
```
🔗 [Perspective Transform Example (docs)](https://docs.opencv.org/4.x/d9/dab/tutorial_py_perspective_transform.html)