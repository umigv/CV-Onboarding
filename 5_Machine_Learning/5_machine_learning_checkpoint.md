# Checkpoint 5 - Machine Learning
Congrats on making it to the **fifth checkpoint**!

* This checkpoint is a google colab notebook with an ML task.
* You will need to get complete the notebook to pass this checkpoint.
* You can use all the resources in this section and go online as well if required.

**Important**: Make a copy of the notebook to your own Google Drive before starting to edit it. You can do this by going to `File -> Save a copy in Drive`. The changes you make in the original notebook will not be saved.

[Click here to access the checkpoint](https://colab.research.google.com/drive/1_E32w1jiCfFxuB8-j7od47pGbV6aa7Pl?usp=sharing)

You will the need the following guide to help you modify the U-Net architecture in the notebook.

# 🛠️ U-Net Modification Guide

This guide explains **where and how** you can modify the `UNet` class to experiment with different design choices.  
Your goal is to **document at least 3 different versions** and compare their training/validation results.

---

## 🔹 1. Encoder / Decoder Depth
- The **contracting path** (`enc1`, `enc2`, `enc3`, `enc4`) and the **expansive path** (`dec4`, `dec3`, `dec2`, `dec1`) define the **depth** of the U-Net.
- **What you can do:**
  - Add **another encoder/decoder block** (make the network deeper).
  - Remove one block to make it shallower (faster but less capacity).
- 📖 See: [nn.Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html)

---

## 🔹 2. Number of Filters
- Each block doubles or halves the number of channels (64 → 128 → 256 → ...).
- **What you can do:**
  - Change the starting filter size (e.g., from 64 to 32).
  - Use smaller increments for lighter models.
- 📖 See: [nn.Conv2d](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)

---

## 🔹 3. Activation Functions

- **Current:** [`nn.ReLU`](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html)  
- **Alternatives to try:**
  - [`nn.LeakyReLU`](https://pytorch.org/docs/stable/generated/torch.nn.LeakyReLU.html)
  - [`nn.ELU`](https://pytorch.org/docs/stable/generated/torch.nn.ELU.html)
  - [`nn.SiLU`](https://pytorch.org/docs/stable/generated/torch.nn.SiLU.html) (aka *Swish*, often used in YOLOv5/6/7)

📍 **File sections:** in `conv_block`

---

## 🔹 4. Normalization Layers

- **Current:** [`nn.BatchNorm2d`](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm2d.html)  
- **Alternatives to try:**
  - [`nn.GroupNorm`](https://pytorch.org/docs/stable/generated/torch.nn.GroupNorm.html)
  - [`nn.InstanceNorm2d`](https://pytorch.org/docs/stable/generated/torch.nn.InstanceNorm2d.html)

💡 **Effect:** Can stabilize training, sometimes better for small batches.  

📍 **File sections:** in `conv_block`

---

## 🔹 5. Dropout

- **Status:** Optional, controlled by `use_dropout=True` when creating the model.  
- **Location:** At the end of each `conv_block`.  
- Enable dropout by setting:  
  ```python
  model = UNet(..., use_dropout=True)
  ```

**What you can do:**
- Change dropout rate (e.g., `0.3 → 0.5`).  
- Disable dropout for baseline vs. enable it for regularization.  

📖 See: [nn.Dropout2d](https://pytorch.org/docs/stable/generated/torch.nn.Dropout2d.html)

---

## 🔹 6. Residual Connections

- **Controlled by:** `use_residual=True`  
- **Location:** At the very end of the forward pass.  

**What you can do:**
- Enable residual connections:  
  ```python
  model = UNet(..., use_residual=True)
  ```
- Compare with/without residuals to see if performance improves.  

📖 See: [ResNet paper summary in torchvision](https://pytorch.org/vision/stable/models/generated/torchvision.models.resnet18.html)

---

## ✅ Suggested Experiments

- **Version A (Baseline):** ReLU + BatchNorm, no dropout, no residual.  
- **Version B:** Add dropout (0.3) + LeakyReLU.  
- **Version C:** Deeper network (add an encoder/decoder block) + residual connections.  

---

## 📌 Documentation Tips

- Record **model configuration** (what you changed).  
- Track **training/validation accuracy or loss curves**.  
- Collect **qualitative results** (predicted masks).  

⚠️ **Tip:** Only change *one thing at a time* so you can clearly see its effect!
