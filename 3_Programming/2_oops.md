# 🧱 Python OOP: Classes and Objects

Object-Oriented Programming (OOP) helps you **organize code** by grouping data and behavior into **objects**.  
It's widely used in computer vision (CV) to model real-world entities like cameras, vehicles, and image processors.

---

## 🧠 Why OOP?

When building software for an **autonomous robotic vehicle (ARV)**, OOP helps you:

- 🚗 **Model real-world components** like cameras, sensors, motors, and controllers as software objects  
- 🧱 **Create reusable blueprints** (classes) for parts of the vehicle (e.g., a `Lidar` class or a `NavigationSystem`)  
- 🧼 **Organize complex logic** into clean, modular code — making it easier to debug, test, and extend  
- 📦 **Store global variables in objects** instead of passing them around everywhere.  
  For example, you don’t need to pass `frame` or `occupancy_grid` into every function — you can store them in `self.frame` and `self.occ_grid` inside a class.  

---

## 🏗️ Classes and Objects

### ✅ Defining a Class
A class is like a blueprint for creating objects.  
Here’s an example where we store the camera frame and occupancy grid in a class. Each part of the following code is explained below:

```python
class PerceptionSystem:
    def __init__(self, frame=None, occ_grid=None):
        self.frame = frame          # stores the latest camera frame
        self.occ_grid = occ_grid    # stores the occupancy grid

    def process_frame(self):
        if self.frame is not None:
            print("Processing camera frame...")
        else:
            print("No frame available.")

    def update_occ_grid(self):
        if self.occ_grid is not None:
            print("Updating occupancy grid...")
        else:
            print("No occupancy grid available.")
```

### 🛠️ Creating an Object

To create an object (an instance of a class), call the class like a function:

```python
# Create an object of PerceptionSystem
ps = PerceptionSystem(frame="dummy_frame", occ_grid="dummy_grid")

# Call its methods
ps.process_frame()      # Output: Processing camera frame...
ps.update_occ_grid()    # Output: Updating occupancy grid...
```

### 🎯 Methods

Methods are just functions inside a class that operate on the object’s data.

```python
def process_frame(self):
    print("Processing camera frame...")
```

Call them using the object:

```python
ps.process_frame()
```

### 📦 `__init__` Method

This special method runs when you create an object.
It sets up initial values like frame or occ_grid:

```python
class PerceptionSystem:
    def __init__(self, frame=None, occ_grid=None):
        self.frame = frame
        self.occ_grid = occ_grid
```

### 🧠 `self` Keyword

`self` refers to the current object.
It’s how you access attributes and methods inside the class.

```python
class PerceptionSystem:
    def process_frame(self):
        print(f"Working with {self.frame}")
```

### 🔄 Updating Attributes

You can modify object attributes directly:

```python
ps.frame = "new_camera_frame"
ps.process_frame()  # Now processes the new frame
```

### 🧬 Inheritance

You can create new classes based on existing ones.
For example, let’s extend `PerceptionSystem` to make a specialized `VisionSystem`:

```python
class VisionSystem(PerceptionSystem):
    def detect_objects(self):
        if self.frame:
            print("Running object detection...")
        else:
            print("No frame to detect objects in.")

vs = VisionSystem(frame="frame_data")
vs.process_frame()
vs.detect_objects()
# Output:
# Processing camera frame...
# Running object detection...
```