# For new programmers :  Python Basics: Variables, Loops, and Functions

Understanding Python's core building blocks will help you write clear and modular CV code. This guide walks through **variables**, **loops**, and **functions** — the foundation of most programs.

---

## Variables 

Variables store data that your program can use and modify. Their 'data type' determines what kind of data they hold. For example:

```python
name = "UMARV" # string type
speed = 45  # integer type
is_autonomous = True # boolean type

# Check the data type of each variable
print(type(name))  # <class 'str'>
print(type(speed))  # <class 'int'>
print(type(is_autonomous))  # <class 'bool'>

# Anything that starts with '#' in Python in a comment, doesn't do anything for the code logic
```

## Indentation
Python uses indentation (spaces or tabs at the start of a line) to define blocks of code. Unlike other languages that use braces `{}` or keywords like `end`, Python relies purely on indentation to determine structure.

If indentation is inconsistent, Python will throw an `IndentationError`.

❌ Incorrect Indentation:
```python
def greet(name):
print("Hello", name)  # ❌ Error: no indentation
```

✅ Correct Indentation:
```python
def greet(name):
    print("Hello", name)  # ✅ Indented properly
```
📌 Tip: Use 4 spaces (not tabs) for each indentation level. Most editors do this automatically.

## 🔁 Loops

Loops help you repeat actions. Python has two main loop types: for and while.

### ✅ For Loop
Used to iterate over a sequence (like a list or range):

```python
for i in range(5):
    print("Frame:", i)
```
You can also loop through items in a list:
```python
objects = ["cone", "barrel", "sign"]
for obj in objects:
    print("Detected:", obj)
```

### 🔄 While Loop
Repeats as long as a condition is true:

```python
battery = 100
while battery > 0:
    print("Driving...")
    battery -= 10
```

### ⏭ Loop Control Statements
`break`: exit the loop early

`continue`: skip to the next iteration

```python
for i in range(5):
    if i == 3:
        break
    print(i)  # prints 0, 1, 2

for i in range(5):
    if i == 3:
        continue
    print(i)  # skips 3
```

## Functions
Functions let you group code into reusable blocks.

### Basic Function
```python
def greet(name):
    print("Hello,", name)

greet("UMARV")
```
### Return Values
Functions can return results:

```python
def add(a, b):
    return a + b

sum = add(3, 5)
print("Sum:", sum)
```
### Parameters and Defaults

You can provide default values for parameters:

```python
def drive(speed=30):
    print("Driving at", speed, "km/h")

drive()
drive(60)
```

### Real Example: Cone Detection
In a CV context, you might want to detect specific objects like cones. Here's how you could structure that with a function:

```python
def detect_cones(objects):
    for obj in objects:
        if obj == "cone":
            print("Cone detected!")

scene = ["sign", "cone", "barrel"]
detect_cones(scene)
```

