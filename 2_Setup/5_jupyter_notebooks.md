## 📓 Step 4: Use Jupyter Notebooks in VS Code

Jupyter notebooks are a great way to write and test small pieces of code, especially for tasks like:
- Visualizing images and video frames  
- Experimenting with computer vision models  
- Running step-by-step Python code with outputs

---

### 📥 Install the Jupyter Extension

1. Open VS Code  
2. Go to the Extensions view (`Ctrl + Shift + X` / `Cmd + Shift + X`)  
3. Search for `Jupyter` and click **Install**

> 💡 You should already have the Python and Jupyter extensions installed from Step 3

---

### Follow this Short Introduction Video
- Watch this 6-minute video to get started with Jupyter in VS Code:  
  [Jupyter Notebooks in VS Code](https://www.youtube.com/watch?v=suAkMeWJ1yE)
- You can **ignore** the parts about Virtual Environments, Pandas, Dataframes, the Debugger, and Data Wrangler as these haven't been introduced in the onboarding yet or aren't relevant to our work!
---
The below sections cover the same steps as in the video, but in text format for reference.

### 📂 Open or Create a Notebook

1. You can open existing `.ipynb` files from our repos  
2. Or create a new one:  
   `File → New File → Save As → my_notebook.ipynb`
    - You can also create a new notebook by clicking the **New File** icon in the File Explorer Pane and naming it with a `.ipynb` extension.

---

### ▶️ Run Cells

- Click the **▶️ Run** button next to any cell to execute it  
- You can also use `Shift + Enter` to run a cell and move to the next one  
- Output (text, plots, images) appears directly below the cell

---

### ⚙️ Choose Kernel

If your code isn't running:
- Click the top-right **"Select Kernel"** button
- Choose your current Python environment.
- VS Code might ask you to install the ipykernel package if it can't find it. Click **Install** to set it up.

---

## 📓 Colab Notebooks
You can also use Google Colab to run Jupyter notebooks in the cloud without any setup. Just upload your notebook file to [colab.research.google.com](https://colab.research.google.com) and run it there.

We'll use Colab for Checkpoint 4 - Classical CV and Checkpoint 5 - Machine Learning, so this section is just to let you know that it exists.

Google Colab provides free access to GPUs, which allows us to run larger models and datasets than on a local machine. However, Colab has some limitations:
- Sessions can time out after a period of inactivity (usually 30-90 minutes)
- You have limited disk space and RAM
- You need to re-upload files each time you start a new session
- You may need to re-install libraries each time
- You need to be connected to the internet
---