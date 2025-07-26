## 🌱 Step 2: Learn Git & GitHub

Git and GitHub let us **collaborate on code**, track changes, and work on the same projects without conflicts.

You'll use Git to:
- Clone the UMARV repositories  
- Create your own branches  
- Push your code for review  
- Pull updates from the team

---

Some important terms:
- **Repository (repo)**: A project folder with all its files and history.
- **Branch**: A separate line of development. You can work on features without affecting the main code.
- **Commit**: A snapshot of your changes. You can add messages to describe what you changed.
- **Pull Request (PR)**: A request to merge your changes into the main codebase. Team members review it before merging.
- **Merge**: Combining changes from one branch into another.
- **Clone**: Copying a repository to your local machine to work on it.
- **Push**: Sending your local changes to the remote repository on GitHub.
- **Pull**: Fetching the latest changes from the remote repository to your local machine.
- **Remote**: The version of your repository hosted on GitHub.
- **Local**: The version of your repository on your own computer.
---

### 📥 Install Git

1. Download Git from the official site:  
   [https://git-scm.com/downloads](https://git-scm.com/downloads)

2. Choose the installer for your operating system:  
   - **Windows**: Click Windows and download the **Git for Windows/x64 Setup.**
   - **macOS**: Click macOS and download using Homebrew:  
     ```bash
     brew install git
     ```
     - If you don't have Homebrew, install it first:  
       [https://brew.sh/](https://brew.sh/)

---

### 🔐 Set Up Git (first time only)

Open a terminal and configure your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
This sets your identity for commits.

### 🐙 Create a GitHub Account

1. Sign up here:  
   [https://github.com/join](https://github.com/join)

2. Set your **username** and **email** — this is where your code will be stored online and shared with the team.

3. Ask us (Maya or Pranav) to add you to the UMARV GitHub organization.  
   - This gives you access to our repositories.

### GitHub Cheatsheet
Link to the full cheatsheet: 
[GitHub Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)

Here's a quick reference for common Git commands:

```bash
# Clone a repository
git clone <repo-url>

# Create a new branch
git checkout -b <branch-name>

# Switch to an existing branch
git checkout <branch-name>

# Add changes to staging
git add <file-or-directory>

# Commit changes with a message
git commit -m "Your commit message"

# Push changes to the remote repository
git push origin <branch-name>

# Pull the latest changes from the remote repository
git pull origin <branch-name>

# View the status of your repository
git status

# View brief commit history
git log --oneline
