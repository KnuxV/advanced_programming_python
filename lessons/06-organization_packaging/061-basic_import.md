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
