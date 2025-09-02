# Python Organization and Packaging: Complete Class Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Module vs Script vs Library](#module-vs-script-vs-library)
3. [The Python Import System](#the-python-import-system)
4. [Working with Packages](#working-with-packages)
5. [Creating Your Own Package](#creating-your-own-package)
6. [Publishing to PyPI](#publishing-to-pypi)
7. [Hands-On Exercises](#hands-on-exercises)
8. [Quick Reference](#quick-reference)

---

## Introduction

Python's organization system is built around modules and packages, which allow you to structure your code in a maintainable and reusable way. This class will take you from understanding basic imports to publishing your own package on PyPI.

### Learning Objectives
- Understand the difference between modules, scripts, and libraries
- Master Python's import system
- Create and structure your own packages
- Publish packages to PyPI for public use

---

## Module vs Script vs Library

### Module
A **module** is any Python file (`.py`) that contains Python code. It can define functions, classes, and variables, and can also include runnable code.

```python
# math_utils.py (this is a module)
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

### Script
A **script** is a Python file that's meant to be executed directly. It typically performs a specific task when run.

```python
# process_data.py (this is a script)
import pandas as pd

def main():
    data = pd.read_csv('data.csv')
    print(f"Processed {len(data)} rows")

if __name__ == "__main__":
    main()
```

### Library
A **library** is a collection of modules that provide related functionality. Libraries are meant to be imported and used by other code, not run directly.

### Key Rule of Thumb
- **Scripts** are meant to be run: `python script.py`
- **Libraries** are meant to be imported: `import library`
- **Modules** can be both, but should generally focus on one role

---

## The `if __name__ == "__main__"` Pattern

### What is `__main__`?

When Python runs a file, it sets special variables. One of these is `__name__`. This variable changes depending on how the file is used:
- If the file is run directly: `__name__ = "__main__"`
- If the file is imported: `__name__ = "module_name"`

### Why We Use It

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Calculator loaded!")
result = add(5, 3)
print(f"5 + 3 = {result}")
```

**Problem without `__main__`:** Every time someone imports this module to use the `add` function, those print statements will execute!

```python
# another_file.py
from calculator import add  # This will print "Calculator loaded!" and "5 + 3 = 8"
```

**Solution with `__main__`:**
```python
# calculator.py (improved)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    # This only runs when the file is executed directly
    print("Calculator loaded!")
    result = add(5, 3)
    print(f"5 + 3 = {result}")
```

Now when someone imports it:
```python
# another_file.py
from calculator import add  # Nothing prints! Just imports the function
```

### Common Use Cases

1. **Testing code in a module:**
```python
# my_module.py
def complex_function(x):
    return x ** 2 + 2 * x + 1

if __name__ == "__main__":
    # Test the function when running the file directly
    test_values = [1, 2, 3, 4, 5]
    for val in test_values:
        print(f"f({val}) = {complex_function(val)}")
```

2. **Creating dual-purpose files (can be imported OR run):**
```python
# web_scraper.py
import requests

def scrape_website(url):
    response = requests.get(url)
    return response.text

def main():
    url = input("Enter URL to scrape: ")
    content = scrape_website(url)
    print(f"Retrieved {len(content)} characters")

if __name__ == "__main__":
    main()  # Only runs when executed as a script
```

---

## The Python Import System

### Understanding the Python Path

The **Python Path** (`sys.path`) is a list of directory locations where Python looks for modules when you use an `import` statement. Think of it as Python's search directories - just like how your computer searches for programs in specific folders.

```python
import sys
print(sys.path)
# Output example:
# ['',  # Empty string = current directory
#  '/usr/local/lib/python39.zip',
#  '/usr/local/lib/python3.9',
#  '/usr/local/lib/python3.9/lib-dynload',
#  '/home/user/.local/lib/python3.9/site-packages',
#  '/usr/local/lib/python3.9/site-packages']
```

### How Python Finds Modules

When you write `import something`, Python searches in this order:
1. **Built-in modules** (like `math`, `os`) - These are compiled into Python
2. **Current directory** - The folder where your script is located
3. **PYTHONPATH directories** - Folders you've added to the PYTHONPATH environment variable
4. **Standard library** - Python's installation directory (e.g., `/usr/lib/python3.9`)
5. **Site-packages** - Where pip installs third-party packages

If Python doesn't find the module in any of these locations, you get a `ModuleNotFoundError`.

### Import Statements

#### Basic Import
```python
import math
print(math.sqrt(16))  # 4.0
```

#### Import with Alias
```python
import pandas as pd
df = pd.DataFrame()
```

#### Specific Import
```python
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793
```

#### Import All - Why You Should Avoid It
```python
from math import *
print(cos(0))  # 1.0
```

### Why Avoid `import *`?

Using `from module import *` is generally bad practice for several reasons:

1. **Namespace Pollution**: It dumps everything into your namespace
```python
# BAD: What does this file have access to?
from math import *
from statistics import *
from numpy import *  # Now which 'mean' function are we using?

mean([1, 2, 3])  # math.mean? statistics.mean? numpy.mean?
```

2. **Readability**: Others (including future you) can't tell where functions come from
```python
# BAD: Where do these come from?
from mystery_module import *
result = process(data)  # What module is 'process' from?
value = calculate(10)   # What module is 'calculate' from?

# GOOD: Clear origin
import mystery_module
result = mystery_module.process(data)
```

3. **Name Conflicts**: Can silently override your variables
```python
# Your code
def sum(numbers):
    return "Sum is: " + str(sum(numbers))

from math import *  # This imports math.sum and overwrites YOUR sum function!
```

4. **IDE and Linting Issues**: Code editors can't provide good autocomplete or catch errors
```python
from pandas import *  # Your IDE now has to guess what's available
```

5. **Performance**: Imports everything even if you only need one function

**When is `import *` acceptable?**
- Interactive Python sessions for quick testing
- Packages designed for it (like `from tkinter import *` in GUI tutorials)
- When a module explicitly defines `__all__` to limit what's exported

### Importing Your Own Files

#### Same Directory
```python
# file: utils.py
def greet(name):
    return f"Hello, {name}!"

# file: main.py
from utils import greet
print(greet("World"))
```

#### Subdirectory (Package)
```
project/
├── main.py
└── helpers/
    ├── __init__.py
    └── text_utils.py
```

```python
# main.py
from helpers.text_utils import clean_text
# or
import helpers.text_utils
```

#### Parent Directory
```python
import sys
sys.path.append('..')  # Add parent directory to path
from parent_module import something
```

---

## Working with Packages

### What is a Package?

A **package** is a directory containing Python modules and a special `__init__.py` file. The `__init__.py` file (which can be empty) tells Python that the directory should be treated as a package.

### Package Structure
```
mypackage/
├── __init__.py          # Makes it a package
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

### The `__init__.py` File

The `__init__.py` file can:
1. Be empty (just marks the directory as a package)
2. Initialize the package when it's imported
3. Control what's imported with `from package import *`

#### Controlling `import *` Behavior

When someone uses `from your_package import *`, Python needs to know what to import. By default, it would import everything, but you can control this with the `__all__` variable:

```python
# mypackage/__init__.py
from .module1 import function_a, function_b, internal_function
from .module2 import ClassA, ClassB, _PrivateClass

# This controls what gets imported with "from mypackage import *"
__all__ = ['function_a', 'ClassA', 'ClassB']  
# Note: function_b, internal_function, and _PrivateClass are NOT included

__version__ = '1.0.0'
```

Now when someone does:
```python
from mypackage import *

# They get:
# - function_a ✓
# - ClassA ✓  
# - ClassB ✓
# But NOT:
# - function_b ✗
# - internal_function ✗
# - _PrivateClass ✗
```

Without `__all__`:
```python
# If __init__.py has no __all__, then import * would import:
# - Everything that doesn't start with underscore
# - All modules in the package directory
```

#### Using `__init__.py` for Convenience Imports

A common pattern is to use `__init__.py` to provide a cleaner API:

```python
# Without __init__.py shortcuts, users would need to do:
from mypackage.submodule.deeply.nested import ImportantClass
from mypackage.another.deep.module import useful_function

# With __init__.py shortcuts:
# mypackage/__init__.py
from .submodule.deeply.nested import ImportantClass
from .another.deep.module import useful_function

# Now users can simply do:
from mypackage import ImportantClass, useful_function
```

### Relative vs Absolute Imports

#### Absolute Import
```python
from mypackage.subpackage.module3 import function
```

#### Relative Import (only in packages)
```python
from . import module1           # Same directory
from .. import parent_module    # Parent directory
from ..sibling import something  # Sibling directory
```

---

## Creating Your Own Package

### Modern Package Structure

Here's the recommended structure for a Python package in 2024:

```
my-awesome-package/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── pyproject.toml       # Modern configuration file
├── README.md
├── LICENSE
└── .gitignore
```

### The `pyproject.toml` File

#### What is TOML?

TOML (Tom's Obvious Minimal Language) is a configuration file format that's easy to read and write. It's like JSON or YAML but designed to be more human-friendly. Python chose TOML for package configuration because it's clear and simple.

```toml
# This is a comment in TOML
name = "value"              # String
number = 42                 # Integer
floating = 3.14            # Float
boolean = true             # Boolean
array = ["item1", "item2"] # Array/List

[section]                  # This creates a section/table
key = "value"

[section.subsection]       # Nested section
another_key = "another value"
```

#### Modern Package Configuration

This is the modern way to configure Python packages (replaces the older `setup.py`):

```toml
[build-system]
requires = ["setuptools>=65.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my-awesome-package"
version = "0.1.0"
authors = [
    {name = "Your Name", email = "you@example.com"},
]
description = "A short description of your package"
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    "requests>=2.28.0",
    "click>=8.0.0",
]

[project.urls]
Homepage = "https://github.com/yourusername/my-awesome-package"
Issues = "https://github.com/yourusername/my-awesome-package/issues"

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=22.0",
    "mypy>=0.990",
]

[project.scripts]
my-command = "my_package.core:main"  # Creates a CLI command
```

#### Understanding `[project.scripts]`

The `[project.scripts]` section creates command-line commands that users can run after installing your package. Here's how it works:

```toml
[project.scripts]
my-command = "my_package.core:main"
#  ↑                ↑         ↑   ↑
#  |                |         |   |
#  Command    Package  Module  Function
#  name       name
```

This means:
1. After someone installs your package with `pip install my-awesome-package`
2. They can type `my-command` in their terminal
3. Python will run the `main()` function from `my_package/core.py`

Real example:
```python
# src/my_package/core.py
def main():
    print("Hello from my package!")
    # Your CLI logic here

def another_function():
    print("This won't be called by the command")
```

After installation:
```bash
$ my-command
Hello from my package!
```

Multiple commands example:
```toml
[project.scripts]
myapp = "my_package.cli:main"           # Main command
myapp-init = "my_package.cli:init"      # Initialization command  
myapp-clean = "my_package.cli:cleanup"  # Cleanup command
```

Now users have three commands:
```bash
$ myapp         # Runs main()
$ myapp-init    # Runs init()
$ myapp-clean   # Runs cleanup()
```

### Package Code Example

```python
# src/my_package/__init__.py
"""My Awesome Package - A demonstration package."""

from .core import process_data
from .utils import validate_input

__version__ = "0.1.0"
__all__ = ["process_data", "validate_input"]
```

```python
# src/my_package/core.py
"""Core functionality for the package."""

def process_data(data):
    """Process the input data."""
    from .utils import validate_input
    
    if not validate_input(data):
        raise ValueError("Invalid input data")
    
    # Process the data
    return {"processed": data, "status": "success"}

def main():
    """Entry point for the CLI."""
    print("My Awesome Package v0.1.0")
```

```python
# src/my_package/utils.py
"""Utility functions for the package."""

def validate_input(data):
    """Validate input data."""
    return data is not None and len(str(data)) > 0
```

### Installing Your Package Locally

#### Editable Installation (Development Mode)
This creates a link to your package, so changes are reflected immediately:
```bash
pip install -e .
```

#### Regular Installation
```bash
pip install .
```

### Building Your Package

First, install build tools:
```bash
pip install build
```

Then build your package:
```bash
python -m build
```

This creates two files in the `dist/` directory:
- `.tar.gz` - Source distribution
- `.whl` - Wheel (binary) distribution

---

## Publishing to PyPI: Theory and Concepts

### What is PyPI?

**PyPI** (Python Package Index) is the official repository for Python packages. Think of it as Python's app store - it's where developers share their code with the world. When you run `pip install something`, pip downloads the package from PyPI.

### How Package Publishing Works

The publishing process follows these conceptual steps:

1. **Package Creation**: Your code is organized into a standardized structure with metadata
2. **Building**: Your source code is packaged into distribution formats:
   - **Source Distribution (sdist)**: A `.tar.gz` file containing your source code
   - **Wheel**: A `.whl` file (ZIP archive) that's faster to install
3. **Upload**: The built packages are uploaded to PyPI's servers
4. **Distribution**: Other developers can now `pip install` your package

### The Publishing Ecosystem

```
Your Code → Build Process → Distribution Files → PyPI Server → pip install
```

- **Build Tools**: Convert your source code into installable packages (setuptools, poetry, flit)
- **Twine**: Securely uploads your packages to PyPI
- **pip**: Downloads and installs packages from PyPI

### Package Versioning

Packages use **Semantic Versioning**: `MAJOR.MINOR.PATCH`
- **MAJOR**: Breaking changes (1.0.0 → 2.0.0)
- **MINOR**: New features, backward compatible (1.0.0 → 1.1.0)  
- **PATCH**: Bug fixes (1.0.0 → 1.0.1)

### Package Namespacing

Package names on PyPI must be unique. Once someone claims `requests`, no one else can use that name. This is why you'll see packages like:
- `requests` (the original)
- `requests2` (someone else's version)
- `requests-extended` (an extension)

### TestPyPI

TestPyPI is a separate instance of PyPI for testing. It's identical to the real PyPI but:
- It's meant for testing your upload process
- Packages here aren't permanent
- It's safe to make mistakes

### Why Publishing Matters

Publishing your package enables:
- **Code Reuse**: Others can use your solution
- **Collaboration**: Community can contribute improvements
- **Portfolio**: Published packages demonstrate your skills
- **Standardization**: Encourages well-structured, documented code

---

## Hands-On Exercises

### Exercise 1: Create a Simple Module
Create a module called `string_tools.py` with functions to:
- Reverse a string
- Count vowels
- Check if palindrome

### Exercise 2: Build a Package Structure
Create a package called `textanalyzer` with:
- A module for text statistics
- A module for text cleaning
- Proper `__init__.py` files

### Exercise 3: Import Challenge
Given this structure:
```
project/
├── main.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── data/
    ├── __init__.py
    └── loader.py
```
Write the import statements in `main.py` to use functions from both `helpers.py` and `loader.py`.

### Exercise 4: Create and Publish a Package
1. Create a simple package that provides a useful utility
2. Write a proper `pyproject.toml`
3. Build the package
4. Upload to TestPyPI
5. Install and test your package

---

## Quick Reference

### Import Patterns
```python
# Standard import
import module

# Import with alias
import module as alias

# Import specific items
from module import item1, item2

# Import from package
from package.subpackage import module

# Relative imports (inside packages only)
from . import sibling_module
from .. import parent_module
```

### Package Structure Checklist
- [ ] `src/package_name/` directory
- [ ] `__init__.py` files in all package directories
- [ ] `pyproject.toml` with project metadata
- [ ] `README.md` with documentation
- [ ] `LICENSE` file
- [ ] `tests/` directory with test files
- [ ] `.gitignore` for version control

### Publishing Checklist
- [ ] Package builds without errors
- [ ] Version number updated
- [ ] README is complete and formatted correctly
- [ ] All tests pass
- [ ] Package installs correctly locally
- [ ] Tested on TestPyPI
- [ ] API token configured
- [ ] Published to PyPI

### Common Commands
```bash
# Install package in development mode
pip install -e .

# Build package
python -m build

# Check package
twine check dist/*

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ package-name
```

### Debugging Import Issues
```python
# Check Python's import path
import sys
print(sys.path)

# Check module's file location
import module
print(module.__file__)

# Check package's path
import package
print(package.__path__)

# List module contents
import module
print(dir(module))
```

---

## Best Practices

1. **Use meaningful names**: Package and module names should be lowercase, with underscores if needed
2. **Keep imports at the top**: All imports should be at the beginning of the file
3. **Avoid circular imports**: Module A shouldn't import from module B if B imports from A
4. **Use absolute imports**: Prefer absolute imports over relative imports when possible
5. **Document your package**: Include docstrings and a comprehensive README
6. **Version your package**: Use semantic versioning (MAJOR.MINOR.PATCH)
7. **Test before publishing**: Always test on TestPyPI before publishing to PyPI
8. **Use virtual environments**: Develop and test in isolated environments
9. **Include a license**: Always specify how others can use your code
10. **Keep dependencies minimal**: Only include necessary dependencies

---

## Additional Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [PyPI - Python Package Index](https://pypi.org/)
- [Setuptools Documentation](https://setuptools.pypa.io/)
- [Real Python - Publishing Packages](https://realpython.com/pypi-publish-python-package/)
- [PEP 517 - Build System Interface](https://www.python.org/dev/peps/pep-0517/)
- [PEP 621 - Project Metadata](https://www.python.org/dev/peps/pep-0621/)

---

## Conclusion

You now have a comprehensive understanding of Python's organization system, from basic imports to publishing your own packages. Remember that good organization makes your code more maintainable, reusable, and shareable with the Python community. Start small with well-organized modules, build up to packages, and when you create something useful, share it with the world through PyPI!