# 🌱 Virtual Environments

## 📌 Why Virtual Environments?
Virtual environments let you create isolated Python setups so that each project can have its own dependencies without interfering with others.  
This is especially useful when:
- Two projects need **different versions** of the same package.
- You want to avoid **cluttering your global Python installation**.
- Reproducibility matters (e.g., onboarding, assignments, production code).

---

## 🐍 Using `venv` (built-in)

### 1. Create a virtual environment

```bash
python3 -m venv myenv
```
This creates a folder in the current directory named `myenv` containing the isolated Python environment.

### 2. Activate the environment

* **Mac/Linux:**
```bash
source myenv/bin/activate
```
* **Windows (PowerShell)**:
```powershell
myenv\Scripts\Activate.ps1
```

You should see `(myenv)` appear in your terminal prompt — this means the environment is active.

### 3. Install packages inside the env

```bash
pip install numpy opencv-python matplotlib
```

A `requirements.txt` file of a virtual environment usually contains the list of all the packages and their versions of the environment. To install packages from a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Deactivate when done

```bash
deactivate
```

## 🔑 Key Tips

* Name your environment after the project (e.g., `cv-assignment`, `research-env`).

* Always activate the environment before running code.

* Share dependencies using:

    * `pip freeze > requirements.txt`

> **Note:** `conda` is also popular for managing environments. We recommend starting with `venv` since it’s built-in and lightweight.

🔗 [Link to venv docs](https://docs.python.org/3/library/venv.html)

🔗 [Link to conda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)