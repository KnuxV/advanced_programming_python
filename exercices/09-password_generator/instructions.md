---
layout: page
title: "Department SQL Class Exercise"
class_number: 3
date: 2025-08-01
difficulty: "Intermediate"
estimated_time: "90 minutes"
topics: ["sql", "python", "data-analysis"]
---

# Password Generator Exercise

This exercise will help you practice creating command-line interfaces in Python, starting with basic `sys.argv` and progressing to the more powerful `argparse` module.

## Background

We'll build a password generator that creates memorable passwords using random words, inspired by the [XKCD comic about password strength](https://xkcd.com/936/). The idea is that phrases like "correct horse battery staple" are both secure and easier to remember than complex character-based passwords.

![xkcd](../../data/xkcd-password-strength.png)

## Setup

### 1. Download the Word List

You'll need a word list file. Download one of these options:
- **EFF's Long Wordlist**: https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
- **Simple English Wikipedia word list**: https://github.com/first20hours/google-10000-english (use `google-10000-english-no-swears.txt`)

### 2. Project Structure

Create this folder structure:
```
password_generator/
├── data/
│   └── wordlist.txt          # Your downloaded word list
├── starter_code.py           # Provided starter code
├── password_gen_argv.py      # Part 1: Your sys.argv solution
└── password_gen_argparse.py  # Part 2: Your argparse solution
```

### 3. Starter Code

Here's the basic password generation logic (`starter_code.py`):

```python
import random
from pathlib import Path

# Configuration constants
N = 5  # Number of words in the password
SEP = " "  # Separator between words

# Path to word list file
# Path(".") gets the current directory, .parent goes up one level
# Alternative: you could use os.getcwd() or pathlib.Path.cwd()
WORDS_PATH = Path(".") / "data" / "wordlist.txt"

def generate_password(num_words=N, separator=SEP):
    """Generate a password using random words from the word list.
    
    Args:
        num_words (int): Number of words to include in the password
        separator (str): String to use between words
    
    Returns:
        str: The generated password
    """
    # Load word list from file
    with open(WORDS_PATH, "r", encoding="utf-8") as f:
        lst_words = [w.strip() for w in f.readlines()]
    
    # Generate password by randomly sampling words without replacement
    # random.sample() ensures each word appears only once in the password
    result = random.sample(lst_words, k=num_words)
    
    # Join words with separator
    return separator.join(result)

def main():
    """Main function - generates and prints a password with default settings."""
    password = generate_password()
    print(f"Generated password: {password}")

if __name__ == "__main__":
    # Load word list to show basic info
    with open(WORDS_PATH, "r", encoding="utf-8") as f:
        lst_words = [w.strip() for w in f.readlines()]
    
    print(f"Loaded {len(lst_words)} words")
    print("First 5 words:", lst_words[:5])
    
    # Generate and display password
    main()
```

---

## Part 1: Using sys.argv

Create `password_gen_argv.py` by copying the starter code and modifying the `main()` function to accept command-line arguments using `sys.argv`.

### Requirements

Your script should support this usage:
```bash
python password_gen_argv.py 4
# Output: horse battery staple correct

python password_gen_argv.py 6
# Output: apple mountain river cloud forest happy
```

### Expected Functionality

1. **Keep the existing `generate_password()` function** - don't modify it
2. **Modify the `main()` function** to handle command-line arguments from `sys.argv`
3. if the number of words is not specified, use a default of n=5, if n>10, go for n=10

---

## Part 2: Using argparse

Create `password_gen_argparse.py` by copying (use cp) the starter code and replacing the `main()` function to use the `argparse` module for much more sophisticated options.

### Requirements

You can add the `parser = argparse.ArgumentParser(description='My awesome program')` directly in the `__main__`
Your script should support this usage:

```bash
# Basic usage (default: 5 words, space separator, no digits)
python password_gen_argparse.py
# Output: horse battery staple correct

# OPTION: Specify number of words, default n=5
python password_gen_argparse.py -n 6
python password_gen_argparse.py --num-words 6
# Output: apple mountain river cloud forest happy

# OPTION: Different separators (--separator or -s) [space, dash, underscore, slash] only, default space
python password_gen_argparse.py -n 4 --separator dash
# Output: horse-battery-staple-correct

python password_gen_argparse.py -n 4 -s underscore
# Output: horse_battery_staple_correct

python password_gen_argparse.py -n 4 -s slash
# Output: horse/battery/staple/correct

# FLAG: Capitalize words (--capitalize or -c), default False, if present True
python password_gen_argparse.py -n 4 --capitalize
# Output: Horse Battery Staple Correct

python password_gen_argparse.py -n 4 -s dash -c
# Output: Horse-Battery-Staple-Correct

# FLAG: Add random digits (--add-digits or -d) default False if present True
python password_gen_argparse.py -n 4 --add-digits
# Output: horse3 battery7 staple1 correct9

# Combine all options
python password_gen_argparse.py -n 3 -s dash --capitalize --add-digits
# Output: Horse2-Battery5-Correct8
```

### Expected Arguments

1. **`-n, --num-words`**: Number of words (default: 4)
2. **`-s, --separator`**: Separator type with choices: `space`, `dash`, `underscore`, `slash` (default: `space`)
3. **`-c, --capitalize`**: Capitalize each word (flag, default: False)
4. **`-d, --add-digits`**: Add random digit (0-9) after each word (flag, default: False)


### Separator Mapping

You'll need to map the separator names to actual characters:
```python
separator_map = {
    'space': ' ',
    'dash': '-', 
    'underscore': '_',
    'slash': '/'
}
```

### Advanced Features to Include

1. **Input validation**: Ensure number of words is reasonable (1-10)
2. **Error handling**: Graceful handling of invalid separator choices (handled automatically by `choices=`)
3. **Informative help text**: Good descriptions for each argument
4. **Program description**: Explain what the tool does in the help

---

## Testing Your Solutions

### Test Cases for Both Parts

Try these commands to verify your implementations work correctly:

```bash
# Basic functionality
python password_gen_argv.py 3
python password_gen_argparse.py -n 3

# Default behavior (should work for argparse, show usage for argv)
python password_gen_argv.py
python password_gen_argparse.py

# Edge cases
python password_gen_argv.py 1
python password_gen_argparse.py -n 1

# argparse-specific features
python password_gen_argparse.py -n 5 -s dash -c -d
python password_gen_argparse.py --num-words 2 --separator underscore --capitalize

```

