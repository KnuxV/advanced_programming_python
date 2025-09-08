---
layout: page
title: Python Package Management
class_number: 2
---

# Python Package Management: pip, venv, and conda


## Why Package Management Matters

Imagine you're working on two projects:
- Project A needs NumPy version 1.21
- Project B needs NumPy version 1.24

Without proper package management, you'd have conflicts! That's why we use:
- **Package managers** (pip, conda) to install and manage libraries
- **Virtual environments** to isolate project dependencies
- **Requirements files** to share and reproduce environments

By the end of this class, you'll never have to worry about "it works on my machine" problems again.

## Understanding Python Packages

### What's a Package?

A **package** is pre-written code you can use in your projects, instead of writing everything from scratch

### Where Do Packages Come From?

```bash
# PyPI (Python Package Index) - The official repository
# https://pypi.org - Contains 500,000+ packages
pip install pandas  # Downloads from PyPI

# Conda repositories - Anaconda's package repository
# Contains Python and non-Python packages
conda install pandas  # Downloads from conda-forge or defaults

# Git repositories - Install directly from GitHub
pip install git+https://github.com/user/repo.git
```

## pip: Python's Default Package Manager

pip (Pip Installs Packages) comes with Python and is the standard way to install Python packages.

### Basic pip Commands

```bash
# Check if pip is installed and its version
pip --version
pip3 --version  # On some systems, use pip3 for Python 3

# Install packages
pip install numpy                    # Install latest version
pip install pandas==1.5.3           # Install specific version
pip install pandas numpy matplotlib # Install multiple packages

# Upgrade packages
pip install --upgrade pip           # Upgrade pip itself
pip install --upgrade numpy         # Upgrade to latest version

# Uninstall packages
pip uninstall numpy                 # Remove package

# Get information
pip list                            # Show all installed packages
```

### Installing from Requirements Files

Requirements files list all packages your project needs:

```bash
# Create a requirements file
pip freeze > requirements.txt       # Save current environment

# Look at the file
cat requirements.txt
# Output:
# numpy==1.24.0
# pandas==1.5.3
# matplotlib==3.6.2

# Install from requirements file
pip install -r requirements.txt     # Install all listed packages

# Create different requirement files for different purposes
pip freeze > requirements-dev.txt   # Development dependencies
pip freeze > requirements-prod.txt  # Production dependencies
```

### Advanced pip Usage

```bash
# Install packages for current user only (no sudo needed)
pip install --user pandas
```

## Virtual Environments with venv

Virtual environments are isolated Python environments. Each project gets its own set of packages, preventing conflicts.

### Why Use Virtual Environments?

Without virtual environments:
```
Global Python
├── Project A (needs Django 3.2)
├── Project B (needs Django 4.1)  # Conflict!
└── Project C (needs no Django)   # Unnecessary bloat!
```

With virtual environments:
```
Project A/
├── venv/  # Has Django 3.2
Project B/
├── venv/  # Has Django 4.1
Project C/
├── venv/  # Clean, no Django
```

### Creating and Using Virtual Environments

```bash
# Make sure you have venv (usually included with Python 3.3+)
python3 -m venv --help

# Create a virtual environment
python3 -m venv myenv              # Create env named 'myenv'
python3 -m venv venv               # Common convention: name it 'venv'
python3 -m venv ~/envs/project1    # Create in specific location

# Activate the virtual environment
# Linux/Mac:
source myenv/bin/activate           # Activate the environment
# Windows:
myenv\Scripts\activate              # Windows Command Prompt
myenv\Scripts\Activate.ps1          # Windows PowerShell

# You'll see your prompt change:
# Before: username@computer:~/project$
# After:  (myenv) username@computer:~/project$

# Verify you're in the virtual environment
which python                        # Should show path to myenv/bin/python
python --version
pip list                           # Shows only packages in this env

# Install packages (only in this environment)
pip install pandas numpy
pip install -r requirements.txt

# Deactivate when done
deactivate                         # Return to global Python

# Delete a virtual environment (when deactivated)
rm -rf myenv/                      # Just delete the folder!
```

### Virtual Environment Best Practices

```bash
# 1. Always use a virtual environment for projects
cd my_project
python3 -m venv venv
source venv/bin/activate

# 2. Add venv to .gitignore (don't commit it)
echo "venv/" >> .gitignore
# https://github.com/github/gitignore/blob/main/Python.gitignore


# 3. Create requirements.txt for others
pip freeze > requirements.txt
git add requirements.txt  # DO commit this

# 4. Document activation in README
echo "# Setup
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt" > README.md

# 5. Use consistent naming
# Good: venv, .venv, env
# Bad: my_super_special_environment_v2_final
```

### Troubleshooting Virtual Environments

```bash
# Forgot if you're in a virtual environment?
echo $VIRTUAL_ENV                  # Shows path if activated
which python                        # Check which Python you're using

# Wrong Python version?
python3.10 -m venv venv            # Specify Python version
python3.11 -m venv venv --clear    # Recreate with different version

# Can't activate?
# Make sure you're using the right command for your shell
source venv/bin/activate           # bash/zsh (Linux/Mac)

# Package installed globally by mistake?
deactivate                        # Exit virtual env
pip uninstall package_name        # Uninstall from global
source venv/bin/activate          # Re-enter virtual env
pip install package_name          # Install in correct place
```

## Conda: The Scientific Python Manager

Conda is a package manager popular in data science. It can manage Python itself and non-Python dependencies (like C libraries).

### Installing Conda

You have two options:

1. **Miniconda** (Recommended - minimal installation):
```bash
# Download from: https://docs.conda.io/en/latest/miniconda.html
# Linux example:
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
# Follow the prompts, restart terminal after installation
```

2. **Anaconda** (Full distribution with many packages pre-installed):
```bash
# Download from: https://www.anaconda.com/products/distribution
# Includes Jupyter, Spyder, and 250+ packages
# Takes up ~3GB of space
```

### Basic Conda Commands

```bash
# Check installation
conda --version
conda info

# Update conda itself
conda update conda

# List environments
conda env list
conda info --envs

# List packages in current environment
conda list
```

### Creating Conda Environments

```bash
# Create new environment
conda create -n myproject          # Empty environment
conda create -n myproject python=3.10  # With specific Python version
conda create -n datascience python=3.10 pandas numpy jupyter  # With packages

# Activate/deactivate environment
conda activate myproject            # Activate
conda deactivate                   # Return to base

# Your prompt changes to show active environment:
# (base) user@computer:~$          # Default conda environment
# (myproject) user@computer:~$     # Your environment
```

### Managing Packages with Conda

```bash
# Search for packages
conda search pandas
conda search -c conda-forge pandas  # Search specific channel

# Install packages
conda install numpy                # From default channel
conda install pandas=1.5.3         # Specific version
conda install numpy pandas matplotlib  # Multiple packages

# Update packages
conda update numpy
conda update --all                 # Update everything

# Remove packages
conda remove pandas # Remove only in the environment you're in

```

### Environment Files with Conda

```bash
# Export environment to file
conda env export > environment.yml
conda env export --no-builds > environment.yml  # More portable

# Look at the file
cat environment.yml
# Output:
# name: myproject
# channels:
#   - conda-forge
#   - defaults
# dependencies:
#   - python=3.10
#   - numpy=1.24.0
#   - pandas=1.5.3
#   - pip:
#     - some-pip-only-package==1.0.0

# Create environment from file
conda env create -f environment.yml
```


**Best Practice: Use both!**
```bash
# Start with conda for complex dependencies
conda create -n myproject python=3.10
conda activate myproject
conda install numpy pandas scipy  # Scientific packages
pip install some-special-package  # Only on PyPI
# Always use pip AFTER conda installs
```


### When to Use Which?

**Use venv when:**
- Working on web applications
- Simple Python projects
- Teaching/learning Python basics
- Minimal dependencies
- Speed is important

**Use conda when:**
- Data science/machine learning projects
- Need specific Python versions easily
- Complex scientific computing
- Dependencies include C/Fortran libraries
- Working with GPU libraries (CUDA)

## Real-World Workflows



### Data Science Project (conda)

```bash
# 1. Create environment with key packages
conda create -n ds_project python=3.10 jupyter pandas numpy matplotlib seaborn scikit-learn

# 2. Activate and add more packages
conda activate ds_project
conda install -c conda-forge plotly
pip install kaggle  # Not in conda
```

### Mixed Workflow (conda + pip)

```bash
# 1. Use conda for base environment
conda create -n mixed_project python=3.10
conda activate mixed_project

# 2. Install scientific packages with conda
conda install numpy pandas scipy matplotlib

# 3. Install web/special packages with pip
pip install flask redis celery

# 4. Export both conda and pip packages
conda env export > environment.yml
# This file includes both conda and pip packages!
```



### pip Issues

**"Permission denied" when installing**
```bash
# Don't use sudo! Use --user or virtual environment
pip install --user package_name
# Better: use a virtual environment
```

**"No module named pip"**
```bash
# Reinstall pip
python3 -m ensurepip
# Or
curl https://bootstrap.pypa.io/get-pip.py | python3
```

**"Package conflicts" or "incompatible versions"**
```bash
# Create fresh environment
python3 -m venv fresh_env
source fresh_env/bin/activate
pip install -r requirements.txt
```

### venv Issues

**"venv not found" or "No module named venv"**
```bash
# Install python3-venv (Ubuntu/Debian)
sudo apt install python3-venv
# Or use conda instead
```

### conda Issues

**Mixing pip and conda causes issues**
```bash
# Best practice: conda first, then pip
conda install all_conda_packages
pip install only_pip_packages  # At the very end
```

## Best Practices Summary

### 1. Always Use Virtual Environments
```bash
# Never install packages globally
# Bad:  pip install pandas
# Good: source venv/bin/activate && pip install pandas
```

### 2. Document Your Dependencies
```bash
# For pip projects
pip freeze > requirements.txt

# For conda projects  
conda env export --no-builds > environment.yml
```

### 3. Use .gitignore
```bash
# Always exclude environments from git
echo "venv/
*.pyc
__pycache__/
.env" > .gitignore
```

### 4. One Environment Per Project
```bash
# Don't share environments between projects
project1/venv/  # Separate
project2/venv/  # Separate
```

### 5. Keep Environments Clean
```bash
# Periodically rebuild environments
deactivate
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Reference Card

### Daily Commands You'll Actually Use

```bash
# venv workflow
python3 -m venv venv              # Create
source venv/bin/activate          # Enter
pip install package               # Install
pip freeze > requirements.txt     # Save
deactivate                       # Exit

# conda workflow
conda create -n project python=3.10  # Create
conda activate project                # Enter
conda install package                 # Install
conda env export > environment.yml   # Save
conda deactivate                     # Exit

# Check where you are
which python                     # Which Python?
pip list                        # What's installed?
echo $VIRTUAL_ENV              # In venv?
conda info --envs              # Which conda env?
```

## Practice Exercises

### Exercise 1: Create a simple Project Environment
```bash
# Create a Flask web app environment
mkdir web_project && cd web_project
python3 -m venv venv
source venv/bin/activate
pip install pandas sqlite3
pip freeze > requirements.txt
deactivate
```

### Exercise 2: Data Science Setup with Conda
```bash
# Create a data analysis environment
conda create -n data_analysis python=3.10 pandas matplotlib jupyter
conda activate data_analysis
# Launch jupyter notebook
jupyter notebook
# Create a simple analysis
conda deactivate
```

### Exercise 3: Clone and Run a Flask App

**Quick Background:**
- **Git clone**: Downloads a copy of someone else's code repository to your computer
- **Flask**: A Python web framework for building websites and web apps 
- **127.0.0.1:5000**: Your local development server address (localhost port 5000). It's for prototyping. None but you can access the website you're creating.

**Your Task:**
Go to https://github.com/pj8912/todo-app and figure out how to:

1. Clone the repository to your machine
2. Set up the Python environment 
3. Install the dependencies
4. Get the app running
5. Open it in your browser

**What to look for on the GitHub page:**
- The clone URL 
- Setup instructions in the README
- What files you need to run
- Any database setup steps

**Success criteria:** You should see a working todo app in your browser where you can add and delete tasks.

**Hints:** Look for files like `requirements.txt`, `app.py`, and any setup scripts. The README usually has the steps you need.



## Resources

📚 **Documentation:**
- [pip documentation](https://pip.pypa.io/)
- [venv documentation](https://docs.python.org/3/library/venv.html)
- [conda documentation](https://docs.conda.io/)
- [Python Packaging Guide](https://packaging.python.org/)

🛠 **Tools to Explore:**
- [pipenv](https://pipenv.pypa.io/) - Combines pip and venv
- [poetry](https://python-poetry.org/) - Modern dependency management
- [mamba](https://mamba.readthedocs.io/) - Fast conda alternative
- [pip-tools](https://pip-tools.readthedocs.io/) - Better requirements management

---
