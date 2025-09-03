# Python Command-Line Arguments: Complete Class Guide

## Table of Contents
1. [Introduction](#introduction)
2. [What is a CLI?](#what-is-a-cli)
3. [Understanding sys.argv](#understanding-sysargv)
4. [Introduction to argparse](#introduction-to-argparse)
5. [Building Advanced CLIs](#building-advanced-clis)
6. [Real-World Patterns](#real-world-patterns)
7. [Best Practices](#best-practices)
8. [Hands-On Exercises](#hands-on-exercises)
9. [Quick Reference](#quick-reference)

---

## Introduction

Command-line interfaces (CLIs) are powerful tools that allow users to interact with your Python programs through the terminal. This class will take you from understanding basic command-line arguments to building professional-grade CLI applications.

### Learning Objectives
- Understand what CLIs are and why they're important
- Master `sys.argv` for basic argument handling
- Build sophisticated CLIs with `argparse`
- Create professional command-line tools
- Handle complex argument patterns and validation

---

## What is a CLI?

### Command-Line Interface Basics

A **Command-Line Interface (CLI)** is a text-based way to interact with programs. Instead of clicking buttons in a graphical interface, users type commands and arguments.

#### CLI vs GUI
```bash
# CLI approach
$ convert image.jpg --resize 800x600 --quality 85 output.jpg

# GUI approach would require:
# 1. Open application
# 2. Click "File" → "Open" → browse to image.jpg
# 3. Click "Image" → "Resize" → type 800, 600
# 4. Click "File" → "Export" → set quality to 85
# 5. Choose location and save
```

### Why CLIs Matter

1. **Automation**: Can be scripted and chained together
```bash
# Process hundreds of files automatically
for file in *.jpg; do
    convert "$file" --resize 800x600 "resized_$file"
done
```

2. **Speed**: No GUI overhead, direct execution
3. **Remote Access**: Works over SSH, no display needed
4. **Composability**: Unix philosophy - small tools that do one thing well
```bash
# Combine tools with pipes
$ cat data.txt | grep "error" | wc -l  # Count error lines
```

5. **Reproducibility**: Commands can be documented and shared
```bash
# Share exact command with colleague
python analyze.py --input data.csv --method regression --output results.pdf
```

### Anatomy of a CLI Command

```bash
$ python script.py positional --flag --option value --verbose
  ↑      ↑         ↑          ↑      ↑        ↑      ↑
  |      |         |          |      |        |      |
Program Script  Positional  Flag  Option  Value  Flag
               argument          (with value)   (boolean)
```

Real example:
```bash
$ git commit -m "Initial commit" --all
  ↑    ↑      ↑   ↑                ↑
  |    |      |   |                |
Program |   Option Message      Flag
     Subcommand
```

## Command-Line Argument Types

Before diving into implementation details, let's clarify the different types of command-line arguments:

```bash
python script.py input.txt -v --output result.txt --format json
                    ↑      ↑      ↑       ↑         ↑       ↑
                positional flag  option  value    option  value
```

**Dash conventions:**
- **Single dash** (`-v`, `-o`): Short form, typically one letter
- **Double dash** (`--verbose`, `--output`): Long form, full words for readability
- Most arguments support both: `-v` and `--verbose` do the same thing

**Argument types:**
- **Flags** (`-v`, `--verbose`): **Boolean** switches that are either present or absent
- **Options** (`-o file.txt`, `--output file.txt`): Take values and modify behavior

Both flags and options can use single or double dashes, but options require additional values while flags don't.

**Common flag conventions:**
- `-v`, `--verbose`: Enable detailed output
- `-q`, `--quiet`: Suppress output  
- `-f`, `--force`: Skip confirmations
- `-h`, `--help`: Show help message
- `-n`, `--dry-run`: Show what would happen without doing it
- `-r`, `--recursive`: Process directories recursively

---

## Understanding sys.argv

### What is sys.argv?

`sys.argv` is a list containing the command-line arguments passed to a Python script. It's the most basic way to handle command-line input.

```python
# script.py
import sys
print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")
print(f"Number of arguments: {len(sys.argv) - 1}")
```

Running it:
```bash
$ python script.py hello world 123
Script name: script.py
Arguments: ['hello', 'world', '123']
Number of arguments: 3
```

### Key Points About sys.argv

1. **argv[0] is always the script name** (or path to the script)
2. **All arguments are strings** - even numbers need conversion
3. **Includes everything** - flags, options, values all mixed together
4. **Order matters** - arguments are positional

### Basic sys.argv Examples

#### Example 1: Simple Calculator
```python
# calc.py
import sys

if len(sys.argv) != 4:
    print("Usage: python calc.py <number1> <operator> <number2>")
    print("Example: python calc.py 10 + 5")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    operator = sys.argv[2]
    num2 = float(sys.argv[3])
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            sys.exit(1)
        result = num1 / num2
    else:
        print(f"Unknown operator: {operator}")
        print("Supported operators: +, -, *, /")
        sys.exit(1)
    
    print(f"{num1} {operator} {num2} = {result}")
    
except ValueError:
    print("Error: Please provide valid numbers")
    sys.exit(1)
```
#TODO Try extending this calculator to support sin, cos operations!


Usage:
```bash
$ python calc.py 10 + 5
10.0 + 5.0 = 15.0

$ python calc.py 20 "*" 3  # Note: * needs quotes in bash
20.0 * 3.0 = 60.0

$ python calc.py sin(60) # radians, degrees ? 
$ python calc.py cos(60) --units degrees # add an option to specify units
$python calc.py tan(0.5) -u rad # short option

```

#### Example 2: File Processor
```python
# process_files.py
import sys
import os

def process_file(filepath):
    """Process a single file."""
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found")
        return False
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    print(f"File: {filepath}")
    print(f"  Lines: {len(lines)}")
    print(f"  Size: {os.path.getsize(filepath)} bytes")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python process_files.py <file1> [file2] [file3] ...")
        print("Process one or more files and display statistics")
        sys.exit(1)
    
    # Process each file provided
    files = sys.argv[1:]
    success_count = 0
    
    for filepath in files:
        if process_file(filepath):
            success_count += 1
        print()  # Empty line between files
    
    print(f"Successfully processed {success_count}/{len(files)} files")

if __name__ == "__main__":
    main()
```

### Limitations of sys.argv

While `sys.argv` works for simple cases, it has significant limitations:

1. **No built-in help**: You must manually write usage instructions
2. **No validation**: All checking is manual
3. **No type conversion**: Everything is a string
4. **Poor organization**: Mixing flags, options, and positional args is messy
5. **No standard parsing**: Each script reinvents the wheel

Example of complexity with sys.argv:
```python
# Trying to handle flags with sys.argv becomes messy
import sys

verbose = False
output_file = None
input_files = []

i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == '-v' or arg == '--verbose':
        verbose = True
        i += 1
    elif arg == '-o' or arg == '--output':
        if i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]
            i += 2
        else:
            print("Error: -o requires a filename")
            sys.exit(1)
    elif arg.startswith('-'):
        print(f"Unknown option: {arg}")
        sys.exit(1)
    else:
        input_files.append(arg)
        i += 1

# This is getting complicated and we haven't even added:
# - Short flag combinations (-vo instead of -v -o)
# - Default values
# - Type checking
# - Subcommands
# - Help text generation
```

This is why we use `argparse`!

---

## Introduction to argparse

### What is argparse?

`argparse` is Python's standard library module for creating professional command-line interfaces. It handles all the complexity of parsing arguments and provides many features automatically.

### Basic argparse Structure

```python
import argparse

# 1. Create the parser
parser = argparse.ArgumentParser(description='My awesome program')

# 2. Add arguments
parser.add_argument('filename', help='File to process')
parser.add_argument('-v', '--verbose', action='store_true', 
                    help='Enable verbose output')

# 3. Parse the arguments
args = parser.parse_args()

# 4. Use the arguments
print(f"Processing {args.filename}")
if args.verbose:
    print("Verbose mode enabled")
```

### Automatic Features

With just those few lines, argparse automatically provides:

```bash
$ python script.py --help
usage: script.py [-h] [-v] filename

My awesome program

positional arguments:
  filename       File to process

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Enable verbose output
```

Error handling:
```bash
$ python script.py
usage: script.py [-h] [-v] filename
script.py: error: the following arguments are required: filename

$ python script.py --invalid
usage: script.py [-h] [-v] filename
script.py: error: unrecognized arguments: --invalid
```

### Types of Arguments

#### 1. Positional Arguments
Required arguments that must appear in a specific order.

```python
parser.add_argument('source', help='Source file')
parser.add_argument('destination', help='Destination file')

# Usage: python script.py input.txt output.txt
# args.source = 'input.txt'
# args.destination = 'output.txt'
```

#### 2. Optional Arguments (Flags/Options)
Arguments that start with `-` or `--`. Can be flags (boolean) or take values.

```python
# Flag (boolean) - using action='store_true'
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Enable verbose output')

# Option with value
parser.add_argument('-o', '--output', type=str,
                    help='Output filename')

# Usage: python script.py -v -o result.txt
# args.verbose = True
# args.output = 'result.txt'
```

#### 3. Optional with Default Values
```python
parser.add_argument('-n', '--number', type=int, default=10,
                    help='Number of iterations (default: %(default)s)')

# If not provided: args.number = 10
# If provided: python script.py -n 20 → args.number = 20
```

### Argument Actions

The `action` parameter controls what happens when an argument is encountered:

```python
# store_true: Set to True if flag is present
parser.add_argument('--verbose', action='store_true')

# store_false: Set to False if flag is present
parser.add_argument('--no-cache', action='store_false', dest='cache')

# store_const: Store a constant value
parser.add_argument('--mode-fast', action='store_const', 
                    const='fast', dest='mode')

# append: Accumulate values into a list
parser.add_argument('--include', action='append',
                    help='Include a file (can be used multiple times)')
# python script.py --include a.txt --include b.txt
# args.include = ['a.txt', 'b.txt']

# count: Count how many times an argument appears
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='Increase verbosity (-vvv for level 3)')
# python script.py -vvv → args.verbose = 3
```

### Type Conversion and Validation

```python
# Built-in type conversion
parser.add_argument('--port', type=int, help='Port number')
parser.add_argument('--ratio', type=float, help='Ratio value')

# Custom type function
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

parser.add_argument('--count', type=positive_int, 
                    help='Positive integer count')

# File type - automatically handles opening files
parser.add_argument('--input', type=argparse.FileType('r'),
                    help='Input file')
parser.add_argument('--output', type=argparse.FileType('w'),
                    help='Output file')
```

### Choices and Constraints

```python
# Limit to specific choices
parser.add_argument('--format', choices=['json', 'xml', 'csv'],
                    default='json',
                    help='Output format')

# Required optional argument (sounds contradictory but useful!)
parser.add_argument('--config', required=True,
                    help='Configuration file (required)')

# Mutually exclusive group
group = parser.add_mutually_exclusive_group()
group.add_argument('--verbose', action='store_true')
group.add_argument('--quiet', action='store_true')
# Can't use both --verbose and --quiet
```

### Comprehensive Example

```python
#!/usr/bin/env python3
"""
File processor with comprehensive CLI.
"""
import argparse
import sys
from pathlib import Path

def create_parser():
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description='Process files with various options',
        epilog='Example: %(prog)s input.txt -o output.txt --format json -v',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Positional arguments
    parser.add_argument('input_file', 
                        type=Path,
                        help='Input file to process')
    
    # Optional arguments
    parser.add_argument('-o', '--output',
                        type=Path,
                        help='Output file (default: stdout)')
    
    parser.add_argument('-f', '--format',
                        choices=['json', 'xml', 'csv', 'text'],
                        default='text',
                        help='Output format (default: %(default)s)')
    
    parser.add_argument('--encoding',
                        default='utf-8',
                        help='File encoding (default: %(default)s)')
    
    # Processing options
    processing_group = parser.add_argument_group('processing options')
    processing_group.add_argument('--skip-empty',
                                  action='store_true',
                                  help='Skip empty lines')
    processing_group.add_argument('--limit',
                                  type=int,
                                  metavar='N',
                                  help='Process only first N lines')
    
    # Verbosity
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument('-v', '--verbose',
                                  action='count',
                                  default=0,
                                  help='Increase verbosity (-vvv for debug)')
    verbosity_group.add_argument('-q', '--quiet',
                                  action='store_true',
                                  help='Quiet mode')
    
    # Advanced feature: multiple values
    parser.add_argument('--exclude',
                        action='append',
                        default=[],
                        help='Patterns to exclude (can be used multiple times)')
    
    return parser

def main():
    """Main function."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Check if input file exists
    if not args.input_file.exists():
        parser.error(f"Input file does not exist: {args.input_file}")
    
    # Set verbosity level
    if args.quiet:
        verbosity = -1
    else:
        verbosity = args.verbose
    
    # Process based on arguments
    if verbosity >= 1:
        print(f"Processing: {args.input_file}")
        print(f"Format: {args.format}")
        if args.output:
            print(f"Output: {args.output}")
        if args.exclude:
            print(f"Excluding: {', '.join(args.exclude)}")
    
    # Main processing logic would go here
    with open(args.input_file, 'r', encoding=args.encoding) as f:
        lines = f.readlines()
    
    if args.skip_empty:
        lines = [line for line in lines if line.strip()]
    
    if args.limit:
        lines = lines[:args.limit]
    
    # Output results
    if verbosity >= 0:
        print(f"Processed {len(lines)} lines")

if __name__ == "__main__":
    main()
```

---

