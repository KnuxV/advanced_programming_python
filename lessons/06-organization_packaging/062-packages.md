---
layout: page
title: Packages
class_number: 6
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

