# venv Demo Checklist

## Installing Python (if needed)

**Windows:**
```bash
# Option 1: Microsoft Store (recommended)
# Search "Python" in Microsoft Store and install Python 3.11+

# Option 2: Package manager
winget install Python.Python.3
```

**WSL/Linux:**
```bash
# Update package list
sudo apt update
sudo snap install micro

# Install Python, pip, and venv
sudo apt install python3 python3-pip python3-venv python3-full

# Verify installation
python3 --version
pip3 --version
```

## Pre-Demo Setup (5 min)
- [ ] Open terminal (Git Bash/PowerShell/Terminal)
- [ ] Navigate to desktop or demo folder
- [ ] Check Python is installed: `python --version` or `python3 --version`
- [ ] Check pip works: `pip --version`

## Demo 1: The Problem Without venv (2 min)
- [ ] Show global pip list: `pip list` 
- [ ] Explain: "This is messy - all projects share the same packages"
- [ ] Try to install in the global env <- error
- [ ] Show conflict scenario: "What if Project A needs pandas 1.0 and Project B needs pandas 2.0?"

## Demo 2: Create and Use venv (8 min)
- [ ] Create project folder: `mkdir demo_project && cd demo_project`
- [ ] Create virtual environment: `python -m venv venv`
- [ ] Show what was created: `ls` (point out venv folder)
- [ ] **Key moment:** Activate venv: `source venv/bin/activate` (Linux/Mac) or `source venv/Scripts/activate` (Git Bash)
- [ ] **Show prompt change:** Point out `(venv)` in terminal
- [ ] Verify clean environment: `pip list` (should be minimal)
- [ ] Install some packages: `pip install requests pandas`
- [ ] Install art from art import tprint tprint("PYTHON") and cowsay -t TEXT (straight from terminal)
- [ ] Show packages: `pip list` (now has our packages)
- [ ] Also show the environement in vscode

## Demo 3: Requirements File (3 min)
- [ ] Create requirements: `pip freeze > requirements.txt`
- [ ] Show the file: `cat requirements.txt` or open in editor
- [ ] Explain: "This is how we share our environment with others"

## Demo 4: Deactivate and Show Isolation (2 min)
- [ ] Deactivate: `deactivate`
- [ ] Show prompt change: `(venv)` disappears
- [ ] Show global packages: `pip list` (different from venv)
- [ ] Reactivate to show it works: `source venv/bin/activate`

## Key Teaching Points to Emphasize
- [ ] **Prompt changes** - most visual cue students will use
- [ ] **One venv per project** - don't share between projects
- [ ] **Always activate before installing** - common mistake
- [ ] **requirements.txt is shareable** - venv folder is not
- [ ] **Deactivate when switching projects**

## Quick Troubleshooting Demo (2 min)
- [ ] Show: `which python` (should point to venv when activated)
- [ ] Show common mistake: installing globally by accident
- [ ] Show how to check if in venv: `echo $VIRTUAL_ENV`

## Wrap-up (1 min)
- [ ] Show final workflow cheat sheet:
  ```bash
  python -m venv venv
  source venv/bin/activate  # or venv/Scripts/activate
  pip install cowsay art    # or your actual packages
  pip freeze > requirements.txt
  deactivate
  ```
