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

## 📚 Resources for Further Learning
- [PyTorch Official Documentation](https://pytorch.org/docs/stable/index.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- PyTorch Crash Course: [YouTube](https://www.youtube.com/watch?v=OIenNRt2bjg)
