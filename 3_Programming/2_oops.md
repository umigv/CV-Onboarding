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
A class is like a blueprint for creating objects.  For example, a `Car` class defines what a car is and what it can do. It can `drive`, `stop`, and `honk`. From this blueprint, you can create many car objects (let's say `car1`, `car2`, and so on) which share the same structure and behavior. These can be used in your program (which could race `car1` versus `car2`).

Here’s an example where we store the camera frame and occupancy grid in a class called `ComputerVisionSystem`. Each part of the following code is explained below:

```python
class ComputerVisionSystem:
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

### 🎯 Methods

Methods are just functions inside a class that operate on the object’s data. They define the behavior of the object. Here, `process_frame` and `update_occ_grid` are methods of the `ComputerVisionSystem` class:

```python
def process_frame(self):
    if self.frame is not None:
        print("Processing camera frame...")
    else:
        print("No frame available.")
```

### 📦 `__init__` Method

This special method runs when you create an object. It sets up initial values like frame or occ_grid:

```python
class ComputerVisionSystem:
    def __init__(self, frame=None, occ_grid=None):
        self.frame = frame
        self.occ_grid = occ_grid
```

### 🧠 `self` Keyword

`self` refers to the current object.
It’s how you access attributes and methods inside the class.

```python
class ComputerVisionSystem:
    def print_frame(self):
        print(f"Working with {self.frame}")
```

### 🛠️ Creating an Object

To create an object (an instance of a class), call the class like a function:

```python
# Create an object of ComputerVisionSystem
cvs = ComputerVisionSystem(frame=dummy_frame, occ_grid=dummy_grid)
```

To call its methods, use dot notation:
```python
# Call its methods
cvs.process_frame()      # Output: Processing camera frame...
cvs.update_occ_grid()    # Output: Updating occupancy grid...
```

### 🔄 Updating Attributes

You can modify object attributes directly:

```python
ps.frame = new_camera_frame
ps.process_frame()  # Now processes the new frame
```

### 🧬 Inheritance

You can create new classes based on existing ones.
For example, let’s use `ComputerVisionSystem` to make a specialized `DrivingSystem`:

```python
class DrivingSystem(ComputerVisionSystem):
    def path_plan_using_computer_vision(self):
        self.process_frame()
        print("Planning path using vision data...")
    
    def drive_using_path_plan(self):
        print("Driving the vehicle...")

ds = DrivingSystem(frame="frame_data")
ds.path_plan_using_computer_vision()
ds.drive()
# Output:
# Processing camera frame...
# Planning path using vision data...
# Driving the vehicle...
```