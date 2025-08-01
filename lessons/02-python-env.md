---
layout: page
title: Python Environment Management
---

# Python Environment Management

## Why This Matters

Imagine you're working on three projects: one needs pandas 1.5, another needs pandas 2.0, and a third uses an old library that breaks with new versions. Without environment management, you'll spend more time fixing conflicts than doing economics.

## The Problem: Dependency Hell

```bash
# This scenario will ruin your day:
pip install old_economics_package  # Downgrades numpy to 1.18
pip install new_ml_package         # Needs numpy 1.24+
# Everything breaks
```

## Solution: Isolated Environments

Think of environments like separate workspaces - each project gets its own set of tools.

## Tool #1: venv (Built-in Python)

**Pros:** Simple, comes with Python, lightweight
**Cons:** Only handles Python packages

```bash
# Create environment
python3 -m venv myproject_env

# Activate (Linux/Mac)
source myproject_env/bin/activate

# Activate (Windows)
myproject_env\Scripts\activate

# Install packages
pip install pandas matplotlib requests

# Save your setup
pip freeze > requirements.txt

# Deactivate
deactivate

# Recreate environment later
pip install -r requirements.txt
```

## Tool #2: conda (Data Science Favorite)

**Pros:** Handles Python + system libraries, great for scientific computing
**Cons:** Slower, larger downloads

```bash
# Create environment with specific Python version
conda create -n econ_analysis python=3.11

# Activate
conda activate econ_analysis

# Install packages (conda finds compatible versions)
conda install pandas numpy matplotlib scikit-learn

# Or mix conda + pip
conda install pandas
pip install some_rare_package

# Export environment
conda env export > environment.yml

# Recreate environment
conda env create -f environment.yml

# List environments
conda env list
```

## Tool #3: uv (The New Kid)

**Pros:** Lightning fast, modern Python tooling, simple syntax
**Cons:** Very new, smaller ecosystem

```bash
# Install uv first
pip install uv

# Create project with environment
uv init myproject
cd myproject

# Add packages (automatically manages environment)
uv add pandas matplotlib requests

# Run Python in the environment
uv run python script.py

# Sync environment (like pip install -r requirements.txt)
uv sync
```

## Which Tool to Choose?

**For this course:** Start with **venv** - it's simple and teaches core concepts.

**For data science projects:** Use **conda** - better for complex scientific packages.

**For modern Python development:** Try **uv** - it's the future of Python tooling.

## Practical Workflow

```bash
# 1. Start new project
mkdir gdp_analysis
cd gdp_analysis

# 2. Create environment
python3 -m venv venv
source venv/bin/activate  # Note: venv/bin not myproject_env/bin

# 3. Install what you need
pip install pandas matplotlib jupyter

# 4. Work on your project
python analysis.py

# 5. Save your setup
pip freeze > requirements.txt

# 6. When done
deactivate
```

## VS Code Integration

VS Code automatically detects virtual environments:
1. `Ctrl+Shift+P` → "Python: Select Interpreter"
2. Choose your environment's Python
3. Terminal automatically activates the environment

## Common Gotchas

- **Forgetting to activate:** Your packages won't be found
- **Installing globally:** Pollutes your system Python
- **Wrong pip:** Always check `which pip` after activation
- **Mixing tools:** Don't use conda and pip carelessly together

