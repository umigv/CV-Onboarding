## 🧠 Your First Neural Network: DriveNet

Imagine we want our vehicle to predict **steering angle** and **acceleration** from **sensor readings**.

All neural networks in PyTorch are built using nn.Module. This builds off of the class inheritance from subsection 2: [Object-Oriented Programming](oops.md). The `__init__` method initializes the network's layers, and the `forward` method defines how data flows through the network.

The `Linear` layer used below is what we call a fully connected layer. For this example, we can understand it as a matrix of the shape `(input_features, output_features)`. So, it transforms a vector of `input_features` into a vector of `output_features`.

```math
o_{(8,1)} = A_{(8,2)}i_{(2,1)}
```

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

### 🧩 Key Points to Understand
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
