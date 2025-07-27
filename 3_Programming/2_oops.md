# 🧱 Python OOP: Classes and Objects

Object-Oriented Programming (OOP) helps you **organize code** by grouping data and behavior into **objects**. It's widely used in computer vision (CV) to model real-world entities like cameras, vehicles, and image processors.

---

## 🧠 Why OOP?

When building software for an autonomous robotic vehicle, OOP helps you:

- 🚗 **Model real-world components** like cameras, sensors, motors, and controllers as software objects
- 🧱 **Create reusable blueprints** (classes) for parts of the vehicle (e.g., a `Lidar` class or a `NavigationSystem`)
- 🧼 **Organize complex logic** into clean, modular code — making it easier to debug, test, and extend


---

## 🏗️ Classes and Objects

### ✅ Defining a Class

A class is like a blueprint for creating objects.

```python
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        print(f"The {self.color} car is driving at {self.speed} km/h.")
```
### 🛠️ Creating an Object
To create an object (an instance of a class), you call the class like a function:

```python
car1 = Car("red", 50)
car1.drive()  # Output: The red car is driving at 50 km/h
```

## 🎯 Methods
Methods are functions that live inside a class.

```python
def drive(self):
    print("Driving...")
```

Call them using the object:
```python
car1 = Car("red", 50)
car1.drive()
```
### 📦 __init__ Method
A special method that runs when you create an object. It sets up initial values.

```python
class Car:
def __init__(self, color, speed):
    self.color = color
    self.speed = speed
```

### 🧠 self Keyword
Refers to the current object. It's how you access attributes and methods within the class.

```python
class Car:
    def drive(self):
        print(f"The {self.color} car is driving at {self.speed} km/h.")
```

## 🔄 Updating Attributes
You can modify object attributes directly:
```python
car1.speed = 80
car1.drive()  # Now drives at 80 km/h
```

## 🧬 Inheritance
Create a new class based on an existing one.
```python
class ElectricCar(Car):
    def charge(self):
        print("Charging battery...")

ecar = ElectricCar("blue", 40)
ecar.drive()
ecar.charge()
```