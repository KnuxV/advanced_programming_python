# Hands-On Exercises: Python Modules & Packages

## Exercise : Create Your String Tools Functions
**Goal**: Write simple functions that we'll later turn into a module

Create a new file called `string_tools.py` and write these functions:

```python
def reverse_string(text):
    """
    Reverse a string
    Example: reverse_string("hello") returns "olleh"
    """
    # Your code here
    pass

def count_vowels(text):
    """
    Count vowels (a, e, i, o, u) in a string
    Example: count_vowels("hello") returns 2
    """
    # Your code here
    pass

def is_palindrome(text):
    """
    Check if a string reads the same forwards and backwards
    Example: is_palindrome("racecar") returns True
    """
    # Your code here
    pass
```

**Test your functions** by adding this at the bottom of `string_tools.py`:
```python
if __name__ == "__main__":
    # Test your functions here
    print(reverse_string("hello"))
    print(count_vowels("hello world"))
    print(is_palindrome("racecar"))
```

---

## Exercise 2: Use Your Module
**Goal**: Import and use your functions from another script

Create a new file called `main.py` in the same folder as `string_tools.py`:

```python
# Import your functions here
# Try different import styles:
# 1. import string_tools
# 2. from string_tools import reverse_string
# 3. from string_tools import *

# Test your imported functions
test_word = "python"

# Use your functions and print the results
```

**Questions to explore**:
- What's the difference between `import string_tools` and `from string_tools import reverse_string`?
- How do you call the functions with each import style?

---

## Exercise 3: Convert to a Package Structure
**Goal**: Reorganize your code into a proper package

Create this folder structure:
```
texttools/               # This is your package folder
├── __init__.py         # Makes it a package
├── string_utils.py     # Move your functions here
└── examples.py         # Example usage
```

**Step by step**:
1. Create a folder called `texttools`
2. Create an empty `__init__.py` file inside it
3. Move your functions from `string_tools.py` to `texttools/string_utils.py`
4. Create `texttools/examples.py` with some example usage
5. Update `texttools/__init__.py` to expose your functions:

```python
# In texttools/__init__.py
from .string_utils import reverse_string, count_vowels, is_palindrome

# Optional: define what gets imported with "from texttools import *"
__all__ = ['reverse_string', 'count_vowels', 'is_palindrome']
```

---

## Exercise 4: Use Your Package
**Goal**: Import and use your package from outside its folder

Create a new file called `test_package.py` **outside** the `texttools` folder:

```
your_project/
├── texttools/           # Your package
│   ├── __init__.py
│   ├── string_utils.py
│   └── examples.py
└── test_package.py      # This file
```

In `test_package.py`, try different ways to import:

```python
# Method 1: Import the package
import texttools
result1 = texttools.reverse_string("hello")

# Method 2: Import specific functions
from texttools import count_vowels, is_palindrome
result2 = count_vowels("programming")

# Method 3: Import everything
from texttools import *
result3 = reverse_string("python")

print(f"Reversed: {result1}")
print(f"Vowels: {result2}")
print(f"Reversed again: {result3}")
```

---

## Exercise 5: Add More Features to Your Package
**Goal**: Expand your package with additional functionality

Add a new module `texttools/text_stats.py`:

```python
def word_count(text):
    """Count words in text"""
    # Your code here
    pass

def char_frequency(text):
    """Return a dictionary of character frequencies"""
    # Your code here
    pass

def longest_word(text):
    """Find the longest word in text"""
    # Your code here
    pass
```

Update your `texttools/__init__.py`:
```python
from .string_utils import reverse_string, count_vowels, is_palindrome
from .text_stats import word_count, char_frequency, longest_word

__all__ = [
    'reverse_string', 'count_vowels', 'is_palindrome',
    'word_count', 'char_frequency', 'longest_word'
]
```

Test your expanded package!

---

## Bonus Challenge: Make It Installable
**Goal**: Create a package that can be installed with pip

Create a `pyproject.toml` file in your project root:

```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "texttools-yourname"  # Replace yourname with your actual name
version = "0.1.0"
description = "A simple text processing toolkit"
authors = [{name = "Your Name", email = "your.email@example.com"}]
readme = "README.md"
requires-python = ">=3.7"

[project.urls]
Homepage = "https://github.com/yourusername/texttools"
```

Install your package in development mode:
```bash
pip install -e .
```

Now you can import your package from anywhere!

---

## Reflection Questions
1. What's the difference between a module and a package?
2. Why do we need `__init__.py` files?
3. When would you use `from module import *` vs `import module`?
4. How does Python find your modules and packages?
5. What are the advantages of organizing code into packages?