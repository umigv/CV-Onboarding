# 🔥 PyTorch: Deep Learning Made Easy
PyTorch is one of the most popular deep learning frameworks. It’s perfect for building and training neural networks for computer vision tasks like classification, detection, and segmentation.  

---

## 🧱 Tensors: The Building Blocks of PyTorch  
Tensors are essntially multi-dimensional arrays, but with GPU acceleration.  

They are the fundamental data structure for storing images, labels, and parameters.

### 📦 Creating a Tensor
```python
import torch

# From a list
x = torch.tensor([[1., 2.], [3., 4.]])
print(x)

# Random tensor
y = torch.randn(2, 3)  # shape: 2x3
print(y)
```

### 📐 Shapes of Tensors
Every tensor has a shape, which tells you how many dimensions it has and how many elements are in each dimension.

Examples:
```python
torch.tensor([1, 2, 3]) → shape: (3) → 1D vector with 3 elements

torch.tensor([[1, 2], [3, 4]]) → shape: (2, 2) → 2D matrix with 2 rows and 2 columns

torch.randn(4, 3, 2) → shape: (4, 3, 2) → 3D tensor # (think: 4 images, each 3×2 pixels)
```

Check the shape with:

```python
t = torch.randn(2, 3)
print(t.shape)     # torch.Size([2, 3])
print(t.ndim)      # number of dimensions
```

### 📏 Broadcasting: Making Shapes Match Automatically
Sometimes, you’ll add or multiply tensors of different shapes.
PyTorch automatically "stretches" one tensor so the operation makes sense — this is called broadcasting.

Example 1: **Adding a vector to a matrix**

```python
m = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])   # shape: (2, 3)
v = torch.tensor([10, 20, 30])  # shape: (3,)

print(m + v)
# v is "stretched" to match m's rows:
# [[11, 22, 33],
#  [14, 25, 36]]
```

Example 2: **Adding a scalar to a tensor**

```python
t = torch.tensor([[1, 2], [3, 4]])  # shape: (2, 2)
print(t + 5)
# 5 is "stretched" to every element
```

**Rules of Broadcasting** (simple version):

1. Compare shapes from right to left.
2. Dimensions must be equal or one of them must be 1.
3. If one is 1, it gets stretched to match the other.

## 🧠 Your First Neural Network: DriveNet

Imagine we want our vehicle to predict **steering angle** and **acceleration** from **sensor readings**.

All neural networks in PyTorch are built using nn.Module. This builds off of the class inheritance from subsection 2: [Object-Oriented Programming](oops.md). The `__init__` method initializes the network's layers, and the `forward` method defines how data flows through the network.

The `Linear` layer used below is what we call a fully connected layer. For this example, we can understand it as a matrix of the shape `(input_features, output_features)`. So, it transforms a vector of `input_features` into a vector of `output_features`.

$ o_{(8,1)} = A_{(8,2)}i_{(2,1)} $ 

```python
import torch.nn as nn

class DriveNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(8, 2)  # 8 sensor inputs → 2 outputs (steering, accel)

    def forward(self, sensors):
        return self.fc(sensors)    # predict control commands
```

### 🏋️‍♂️ Training the Network

Come back to this section once you understand the material in Section 5: [Machine Learning](../5_Machine_Learning/).

This is where the magic happens.  
We feed **sensor readings** into our model, compare the predictions to what we *wanted*, and slowly adjust the model to improve its driving decisions.

```python
# 1️⃣ Create our driving model
model = DriveNet()

# 2️⃣ Pick optimizer: Stochastic Gradient Descent                     
optim = torch.optim.SGD(model.parameters(),    
                        lr=0.01) # learning rate controls update size

# 3️⃣ Loss: Mean Squared Error (good for regression)
loss_fn = nn.MSELoss()                         

# 4️⃣ Repeat training for multiple passes
for epoch in range(3):                         
    sensors = torch.randn(4, 8)     # Simulated sensor readings (batch of 4)
    controls = torch.randn(4, 2)    # Desired steering + accel for those readings

    # 5️⃣ Forward pass: model predicts controls
    preds = model(sensors)

    # 6️⃣ Compare predictions to the correct values
    loss = loss_fn(preds, controls)

    # 7️⃣ Reset previous gradients
    optim.zero_grad()

    # 8️⃣ Backpropagate: figure out how wrong we were
    loss.backward()

    # 9️⃣ Update weights to make model better
    optim.step()

    print(f"Epoch {epoch} | Loss: {loss.item():.4f}")

```

### 🧩 What You’re Supposed to Understand Here
By the end of this, you should have a mental map of the training loop:

1. **Model** – Something that takes sensor inputs and predicts commands.
2. **Loss function** – A way to measure “how wrong” the model was.
3. **Optimizer** – A method for improving the model’s parameters based on the loss.
4. **Forward pass** – Feed data into the model to get predictions.
5. **Backward pass (Backprop)** – Figure out which weights caused errors.
6. **Weight update** – Make small changes to reduce future errors.

Think of it like **learning to drive**:
The car drives (forward pass)

* You check if you stayed in lane (loss)
* You figure out what you did wrong (backprop)
* You adjust your driving style for next time (optimizer step)

### 💡 **In UMARV terms:**
We’re basically teaching our vehicle, from past data, how to decide the right steering and acceleration given sensor readings — and every epoch is like another driving lesson.

## 📚 Resources for Further Learning
- [PyTorch Official Documentation](https://pytorch.org/docs/stable/index.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- PyTorch Crash Course: [YouTube](https://www.youtube.com/watch?v=OIenNRt2bjg)
