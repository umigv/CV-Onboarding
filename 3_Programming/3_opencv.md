# 👁️ OpenCV: Fundamentals for Computer Vision

OpenCV is one of the most powerful and widely used libraries for **image processing** and **computer vision**. It gives you tools to read, manipulate, analyze, and extract information from images and videos. Whether you're building object detectors, applying filters, or transforming perspectives, OpenCV is your go-to toolbox.

---
## 🧱 OpenCV Fundamentals

Before diving into advanced techniques, here are the essential building blocks you'll use constantly.

### 📷 Opening an Image

```python
import cv2

img = cv2.imread("image.jpg")
cv2.imshow("My Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 🎥 Opening a Video
```python
cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

```
⚠️ OpenCV reads images and videos in BGR format (not RGB)!

### 🟢 Drawing a Circle
We use this to highlight points of interest or create visual effects.
```python
cv2.circle(img, (100, 100), 30, (0, 255, 0), -1)
```
`(100, 100)` → center

`30` → radius

`(0, 255, 0)` → color (Green in BGR)

`-1` → filled circle

### 📏 Drawing a Line

We use this to connect two points, mark boundaries, or highlight edges.
```python
cv2.line(img, (50, 50), (200, 200), (0, 0, 255), 3)
```

`(50, 50)` → starting point

`(200, 200)` → ending point

`(0, 0, 255)` → color (Red in BGR)

`3` → thickness of the line

### 🔤 Adding Text
We use this to annotate images with labels, instructions, or information.
```python
cv2.putText(img, "Hello", (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 0, 0), 2)
```
`"Hello"` → text

`(50, 50)` → bottom-left corner

`1` → font scale

`(255, 0, 0)` → color (Blue in BGR)

`2` → thickness

---
