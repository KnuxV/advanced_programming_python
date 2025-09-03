
## Building Advanced CLIs

### Subcommands (Like git, docker, aws)

Many professional CLIs use subcommands to organize functionality:
- `git add`, `git commit`, `git push`
- `docker run`, `docker build`, `docker ps`
- `aws s3 cp`, `aws ec2 describe-instances`

```python
#!/usr/bin/env python3
"""
Example: A task management CLI with subcommands.
"""
import argparse
import json
from datetime import datetime
from pathlib import Path

class TaskManager:
    def __init__(self, db_file='tasks.json'):
        self.db_file = Path(db_file)
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if self.db_file.exists():
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, description, priority='medium'):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'priority': priority,
            'created': datetime.now().isoformat(),
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()
        return task['id']
    
    def list_tasks(self, show_completed=False):
        tasks = self.tasks
        if not show_completed:
            tasks = [t for t in tasks if not t['completed']]
        return tasks
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().isoformat()
                self.save_tasks()
                return True
        return False

def create_parser():
    """Create the argument parser with subcommands."""
    parser = argparse.ArgumentParser(
        description='Task management CLI',
        prog='task'
    )
    
    # Global options
    parser.add_argument('--db', 
                        default='tasks.json',
                        help='Database file (default: %(default)s)')
    
    # Create subparsers
    subparsers = parser.add_subparsers(
        title='commands',
        description='Available commands',
        dest='command',
        help='Command help',
        required=True
    )
    
    # 'add' subcommand
    parser_add = subparsers.add_parser('add', 
                                        help='Add a new task')
    parser_add.add_argument('description', 
                            help='Task description')
    parser_add.add_argument('-p', '--priority',
                            choices=['low', 'medium', 'high'],
                            default='medium',
                            help='Task priority (default: %(default)s)')
    
    # 'list' subcommand
    parser_list = subparsers.add_parser('list', 
                                         help='List tasks')
    parser_list.add_argument('-a', '--all',
                             action='store_true',
                             help='Show completed tasks too')
    parser_list.add_argument('--format',
                             choices=['simple', 'detailed', 'json'],
                             default='simple',
                             help='Output format')
    
    # 'complete' subcommand
    parser_complete = subparsers.add_parser('complete',
                                            help='Mark task as complete')
    parser_complete.add_argument('task_id',
                                 type=int,
                                 help='Task ID to complete')
    
    # 'stats' subcommand
    parser_stats = subparsers.add_parser('stats',
                                         help='Show statistics')
    
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    # Initialize task manager
    tm = TaskManager(args.db)
    
    # Execute based on subcommand
    if args.command == 'add':
        task_id = tm.add_task(args.description, args.priority)
        print(f"✓ Task added with ID: {task_id}")
    
    elif args.command == 'list':
        tasks = tm.list_tasks(show_completed=args.all)
        
        if not tasks:
            print("No tasks found")
            return
        
        if args.format == 'json':
            print(json.dumps(tasks, indent=2))
        elif args.format == 'detailed':
            for task in tasks:
                status = "✓" if task['completed'] else "○"
                print(f"{status} [{task['id']}] {task['description']}")
                print(f"  Priority: {task['priority']}")
                print(f"  Created: {task['created']}")
                if task['completed']:
                    print(f"  Completed: {task.get('completed_at', 'Unknown')}")
                print()
        else:  # simple format
            for task in tasks:
                status = "✓" if task['completed'] else "○"
                priority_symbol = {'low': '↓', 'medium': '-', 'high': '↑'}
                p = priority_symbol[task['priority']]
                print(f"{status} [{task['id']}] {p} {task['description']}")
    
    elif args.command == 'complete':
        if tm.complete_task(args.task_id):
            print(f"✓ Task {args.task_id} completed")
        else:
            print(f"✗ Task {args.task_id} not found")
            parser.exit(1)
    
    elif args.command == 'stats':
        total = len(tm.tasks)
        completed = sum(1 for t in tm.tasks if t['completed'])
        pending = total - completed
        
        print("Task Statistics")
        print("=" * 30)
        print(f"Total tasks:     {total}")
        print(f"Completed:       {completed}")
        print(f"Pending:         {pending}")
        if total > 0:
            print(f"Completion rate: {completed/total*100:.1f}%")

if __name__ == "__main__":
    main()
```

Usage examples:
```bash
$ task add "Write documentation" --priority high
✓ Task added with ID: 1

$ task add "Review pull request"
✓ Task added with ID: 2

$ task list
○ [1] ↑ Write documentation
○ [2] - Review pull request

$ task complete 1
✓ Task 1 completed

$ task list --all --format detailed
✓ [1] Write documentation
  Priority: high
  Created: 2024-01-20T10:30:00
  Completed: 2024-01-20T11:45:00

○ [2] Review pull request
  Priority: medium
  Created: 2024-01-20T10:31:00

$ task stats
Task Statistics
==============================
Total tasks:     2
Completed:       1
Pending:         1
Completion rate: 50.0%
```

### Configuration Files

Professional CLIs often support configuration files to set defaults:

```python
import argparse
import configparser
from pathlib import Path

def load_config(config_file='~/.myapp/config.ini'):
    """Load configuration from file."""
    config = configparser.ConfigParser()
    config_path = Path(config_file).expanduser()
    
    # Default configuration
    defaults = {
        'output_format': 'json',
        'verbose': False,
        'timeout': 30,
    }
    
    if config_path.exists():
        config.read(config_path)
        # Override defaults with config file values
        if 'settings' in config:
            for key, value in config['settings'].items():
                if key in defaults:
                    # Convert strings to appropriate types
                    if isinstance(defaults[key], bool):
                        defaults[key] = config.getboolean('settings', key)
                    elif isinstance(defaults[key], int):
                        defaults[key] = config.getint('settings', key)
                    else:
                        defaults[key] = value
    
    return defaults

def create_parser(defaults):
    """Create parser with defaults from config."""
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--format',
                        default=defaults['output_format'],
                        help=f"Output format (default: {defaults['output_format']})")
    
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        default=defaults['verbose'],
                        help='Verbose output')
    
    parser.add_argument('--timeout',
                        type=int,
                        default=defaults['timeout'],
                        help=f"Timeout in seconds (default: {defaults['timeout']})")
    
    # Allow overriding config file location
    parser.add_argument('--config',
                        help='Configuration file path')
    
    return parser

def main():
    # First, parse just the config argument
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument('--config')
    pre_args, remaining = pre_parser.parse_known_args()
    
    # Load config
    config_file = pre_args.config or '~/.myapp/config.ini'
    defaults = load_config(config_file)
    
    # Create main parser with defaults
    parser = create_parser(defaults)
    args = parser.parse_args(remaining)
    
    # Now args contains values from: command line > config file > defaults
    print(f"Format: {args.format}")
    print(f"Verbose: {args.verbose}")
    print(f"Timeout: {args.timeout}")
```

### Environment Variables

Another way to configure CLIs is through environment variables:

```python
import os
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    
    # Check environment variables for defaults
    parser.add_argument('--api-key',
                        default=os.environ.get('MYAPP_API_KEY'),
                        help='API key (or set MYAPP_API_KEY env var)')
    
    parser.add_argument('--endpoint',
                        default=os.environ.get('MYAPP_ENDPOINT', 
                                              'https://api.example.com'),
                        help='API endpoint URL')
    
    parser.add_argument('--debug',
                        action='store_true',
                        default=os.environ.get('MYAPP_DEBUG', '').lower() == 'true',
                        help='Enable debug mode')
    
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.api_key:
        parser.error("API key required. Use --api-key or set MYAPP_API_KEY")
    
    print(f"Using endpoint: {args.endpoint}")
    if args.debug:
        print(f"API Key: {args.api_key[:4]}...")  # Show only first 4 chars
```

---

## Real-World Patterns

### Pattern 1: Verbose Logging Levels

```python
import argparse
import logging

def setup_logging(verbosity):
    """Configure logging based on verbosity level."""
    levels = [
        logging.WARNING,  # 0: Default
        logging.INFO,     # 1: -v
        logging.DEBUG,    # 2: -vv
    ]
    
    level = levels[min(verbosity, len(levels) - 1)]
    
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        if verbosity > 1 else '%(levelname)s: %(message)s'
    )

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose',
                        action='count',
                        default=0,
                        help='Increase verbosity (-vvv for maximum)')
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    setup_logging(args.verbose)
    
    # Now use logging throughout your application
    logging.debug("Debug message (only with -vv)")
    logging.info("Info message (only with -v)")
    logging.warning("Warning message (always shown)")
```

### Pattern 2: Dry Run Mode

```python
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', help='Files to process')
    parser.add_argument('--dry-run', '-n',
                        action='store_true',
                        help="Show what would be done without doing it")
    return parser

def process_file(filepath, dry_run=False):
    if dry_run:
        print(f"[DRY RUN] Would process: {filepath}")
    else:
        print(f"Processing: {filepath}")
        # Actual processing here
        with open(filepath, 'r') as f:
            # Do something
            pass

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if args.dry_run:
        print("DRY RUN MODE - No changes will be made")
        print("-" * 40)
    
    for filepath in args.files:
        process_file(filepath, args.dry_run)
```

### Pattern 3: Interactive Confirmation

```python
import argparse

def confirm(message="Continue?"):
    """Ask for user confirmation."""
    while True:
        response = input(f"{message} [y/N]: ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no', '']:
            return False
        else:
            print("Please enter 'y' or 'n'")

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', '-f',
                        action='store_true',
                        help='Skip confirmation prompts')
    parser.add_argument('--delete',
                        action='store_true',
                        help='Delete files')
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if args.delete:
        if args.force or confirm("Really delete files?"):
            print("Deleting files...")
            # Deletion logic here
        else:
            print("Operation cancelled")
```

### Pattern 4: Progress Indicators

```python
import argparse
import time
from pathlib import Path

# Close file if not stdout
    if args.output != sys.stdout:
        args.output.close()

if __name__ == "__main__":
    main()
```

---

## Best Practices

### 1. Provide Clear Help Text

```python
# Good: Descriptive help with examples
parser = argparse.ArgumentParser(
    description='Process and analyze log files',
    epilog='''Examples:
  %(prog)s access.log --format json
  %(prog)s *.log --filter error --output report.txt
  %(prog)s -vv --from 2024-01-01 --to 2024-01-31 /var/log/app.log
''',
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument('logfile',
                    help='Log file to analyze (supports wildcards)')
parser.add_argument('--filter',
                    help='Filter pattern (e.g., "error", "warning")')
parser.add_argument('--from', dest='from_date',
                    help='Start date (YYYY-MM-DD)')
```

### 2. Use Sensible Defaults

```python
# Good: Defaults that work for most cases
parser.add_argument('--threads',
                    type=int,
                    default=4,
                    help='Number of threads (default: %(default)s)')

parser.add_argument('--timeout',
                    type=float,
                    default=30.0,
                    help='Request timeout in seconds (default: %(default)s)')

# Show defaults in help text using %(default)s
```

### 3. Validate Early

```python
def validate_args(args):
    """Validate arguments after parsing."""
    # Check file existence
    if args.input and not Path(args.input).exists():
        raise ValueError(f"Input file not found: {args.input}")
    
    # Check logical constraints
    if args.start_date and args.end_date:
        if args.start_date > args.end_date:
            raise ValueError("Start date must be before end date")
    
    # Check dependencies
    if args.encrypt and not args.key_file:
        raise ValueError("--encrypt requires --key-file")
    
    return True

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        validate_args(args)
    except ValueError as e:
        parser.error(str(e))
```

### 4. Handle Errors Gracefully

```python
import sys
import traceback

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        # Main logic
        result = process(args)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        return 130  # Standard exit code for SIGINT
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
        
    except PermissionError as e:
        print(f"Permission denied: {e}", file=sys.stderr)
        return 13  # Standard exit code for permission denied
        
    except Exception as e:
        if args.debug:
            traceback.print_exc()
        else:
            print(f"Unexpected error: {e}", file=sys.stderr)
            print("Run with --debug for full traceback", file=sys.stderr)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### 5. Follow Conventions

```python
# Standard short options
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-q', '--quiet', action='store_true')
parser.add_argument('-f', '--force', action='store_true')
parser.add_argument('-n', '--dry-run', action='store_true')
parser.add_argument('-h', '--help')  # Automatic
parser.add_argument('-V', '--version', action='version', 
                    version='%(prog)s 1.0.0')
parser.add_argument('-o', '--output')
parser.add_argument('-i', '--input')

# Use consistent naming
# - Use dashes in long options: --dry-run, not --dry_run
# - Use underscores in dest: dest='dry_run'
parser.add_argument('--log-level', dest='log_level')
```

### 6. Structure for Testing

```python
def create_parser():
    """Create argument parser (separate for testing)."""
    parser = argparse.ArgumentParser()
    # Add arguments
    return parser

def process_args(args):
    """Process parsed arguments (separate for testing)."""
    # Main logic here
    return result

def main(argv=None):
    """Main entry point.
    
    Args:
        argv: Command-line arguments (for testing).
              If None, uses sys.argv.
    """
    parser = create_parser()
    args = parser.parse_args(argv)
    return process_args(args)

if __name__ == "__main__":
    sys.exit(main())

# Now you can test:
# def test_main():
#     result = main(['--input', 'test.txt', '--verbose'])
#     assert result == 0
```

### 7. Use Type Hints

```python
from typing import List, Optional, Any
from pathlib import Path
import argparse

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', type=Path)
    parser.add_argument('--output', type=Path)
    return parser

def process_files(files: List[Path], 
                  output: Optional[Path] = None) -> int:
    """Process files and return exit code."""
    for file in files:
        # Process each file
        pass
    return 0

def main(argv: Optional[List[str]] = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)
    
    return process_files(
        files=args.files,
        output=args.output
    )
```

---

## Hands-On Exercises

### Exercise 1: Basic Calculator CLI

Create a calculator that works like this:
```bash
$ python calc.py add 5 3
8

$ python calc.py multiply 4 7
28

$ python calc.py divide 10 --precision 2 3
3.33
```

Requirements:
- Support add, subtract, multiply, divide operations
- Optional --precision flag for decimal places
- Proper error handling for division by zero

### Exercise 2: File Search Tool

Build a tool that searches for text in files:
```bash
$ python search.py "TODO" *.py
found in main.py:45: # TODO: Add error handling
found in utils.py:12: # TODO: Optimize this function

$ python search.py "error" --ignore-case -r src/
src/app.py:23: raise ValueError("Error in configuration")
src/lib/helpers.py:89: logging.error("Connection failed")
```

Requirements:
- Search pattern as positional argument
- Support wildcards in file patterns
- --ignore-case flag
- -r/--recursive flag for directory search
- --count flag to just show count instead of matches

### Exercise 3: Data Processor with Subcommands

Create a data processing tool with multiple operations:
```bash
$ python data.py stats data.csv
Rows: 1000
Columns: 5
Missing values: 23

$ python data.py filter data.csv --column age --gt 30 -o filtered.csv
Filtered 423 rows

$ python data.py convert data.csv --from csv --to json -o data.json
Converted successfully
```

Requirements:
- Subcommands: stats, filter, convert
- Each subcommand has its own options
- Support multiple file formats
- Progress indicator for large files

### Exercise 4: Configuration Manager

Build a CLI that manages application settings:
```bash
$ python config.py set database.host localhost
✓ Set database.host = localhost

$ python config.py get database.host
localhost

$ python config.py list
database.host = localhost
database.port = 5432
api.timeout = 30

$ python config.py export --format json > settings.json
```

Requirements:
- Subcommands: get, set, list, export, import
- Dot notation for nested settings
- Multiple export formats
- Validation for known settings

### Exercise 5: Advanced Task Runner

Create a task runner with dependencies:
```bash
$ python runner.py --define-task build "echo Building..."
$ python runner.py --define-task test "pytest" --depends-on build
$ python runner.py --define-task deploy "echo Deploying..." --depends-on test

$ python runner.py run deploy
[1/3] Running: build
Building...
[2/3] Running: test
All tests passed
[3/3] Running: deploy
Deploying...
✓ All tasks completed successfully

$ python runner.py list
build: echo Building...
test: pytest (depends on: build)
deploy: echo Deploying... (depends on: test)
```

---

## Quick Reference

### Common argparse Patterns

```python
# Quick template for any CLI script
import argparse
import sys
import logging
from pathlib import Path

def create_parser():
    parser = argparse.ArgumentParser(
        description='Your tool description',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Positional argument
    parser.add_argument('input', help='Input file')
    
    # Optional with value
    parser.add_argument('-o', '--output', help='Output file')
    
    # Flag (boolean)
    parser.add_argument('-v', '--verbose', action='store_true')
    
    # Multiple values
    parser.add_argument('--include', action='append')
    
    # Choice restriction
    parser.add_argument('--mode', choices=['fast', 'slow'])
    
    # Type conversion
    parser.add_argument('--port', type=int, default=8080)
    
    # Count occurrences
    parser.add_argument('-d', '--debug', action='count', default=0)
    
    # Version
    parser.add_argument('--version', action='version', 
                        version='%(prog)s 1.0.0')
    
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    # Setup logging based on verbosity
    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=log_level)
    
    try:
        # Your main logic here
        pass
    except Exception as e:
        logging.error(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### Argument Types Quick Reference

```python
# Built-in types
type=int              # Convert to integer
type=float            # Convert to float  
type=str              # Default, string
type=Path             # pathlib.Path object

# File types
type=argparse.FileType('r')   # Readable file
type=argparse.FileType('w')   # Writable file
type=argparse.FileType('a')   # Appendable file

# Custom type function
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("Must be positive")
    return ivalue

parser.add_argument('--count', type=positive_int)
```

### Actions Quick Reference

```python
action='store'         # Default - store the value
action='store_true'    # Store True if flag present
action='store_false'   # Store False if flag present
action='store_const'   # Store a constant value
action='append'        # Append to list
action='append_const'  # Append constant to list
action='count'         # Count occurrences
action='version'       # Print version and exit
action='help'          # Print help and exit (default for -h)
action='extend'        # Extend list (Python 3.8+)
```

### Special Parameters

```python
# Control argument name in namespace
parser.add_argument('--my-option', dest='my_option')

# Number of arguments
nargs=2          # Exactly 2 arguments
nargs='?'        # 0 or 1 arguments
nargs='*'        # 0 or more arguments
nargs='+'        # 1 or more arguments
nargs=argparse.REMAINDER  # All remaining arguments

# Customize help
metavar='FILE'   # Name shown in help instead of dest
help=argparse.SUPPRESS  # Hide from help

# Requirements
required=True    # Make optional argument required

# Defaults
default='value'  # Default value if not provided
const='value'    # Value when flag used without argument
```

### Exit Codes

```python
# Standard exit codes
0   # Success
1   # General error
2   # Misuse of shell command
126 # Command cannot execute
127 # Command not found
128 # Invalid argument
130 # Script terminated by Ctrl+C

# Usage in Python
import sys

# Success
sys.exit(0)  # or just: return 0

# Error with message
parser.error("Invalid input")  # Exits with code 2

# Custom error
sys.exit(1)  # or: return 1
```

---

## Additional Resources

- [argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [Click Framework](https://click.palletsprojects.com/) - Alternative CLI framework
- [Python Fire](https://github.com/google/python-fire) - Automatic CLI generation
- [Rich](https://github.com/Textualize/rich) - Beautiful terminal output
- [Typer](https://typer.tiangolo.com/) - Modern CLI building on type hints
- [Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)
- [Command Line Interface Guidelines](https://clig.dev/)

---

## Conclusion

You now have a comprehensive understanding of building command-line interfaces in Python, from basic `sys.argv` usage to sophisticated `argparse` applications. Command-line tools are powerful, composable, and essential for automation. Start with simple scripts, gradually add features, and follow the established conventions to create professional tools that others will enjoy using.

Remember: A good CLI is predictable, documented, and follows the principle of least surprise. When in doubt, look at how popular tools like `git`, `docker`, or `aws` handle similar situations, and follow their lead!# Python Command-Line Arguments: Complete Class Guide

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

Usage:
```bash
$ python calc.py 10 + 5
10.0 + 5.0 = 15.0

$ python calc.py 20 "*" 3  # Note: * needs quotes in bash
20.0 * 3.0 = 60.0
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

## Building Advanced CLIs

### Subcommands (Like git, docker, aws)

Many professional CLIs use subcommands to organize functionality:
- `git add`, `git commit`, `git push`
- `docker run`, `docker build`, `docker ps`
- `aws s3 cp`, `aws ec2 describe-instances`

```python
#!/usr/bin/env python3
"""
Example: A task management CLI with subcommands.
"""
import argparse
import json
from datetime import datetime
from pathlib import Path

class TaskManager:
    def __init__(self, db_file='tasks.json'):
        self.db_file = Path(db_file)
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if self.db_file.exists():
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, description, priority='medium'):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'priority': priority,
            'created': datetime.now().isoformat(),
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()
        return task['id']
    
    def list_tasks(self, show_completed=False):
        tasks = self.tasks
        if not show_completed:
            tasks = [t for t in tasks if not t['completed']]
        return tasks
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().isoformat()
                self.save_tasks()
                return True
        return False

def create_parser():
    """Create the argument parser with subcommands."""
    parser = argparse.ArgumentParser(
        description='Task management CLI',
        prog='task'
    )
    
    # Global options
    parser.add_argument('--db', 
                        default='tasks.json',
                        help='Database file (default: %(default)s)')
    
    # Create subparsers
    subparsers = parser.add_subparsers(
        title='commands',
        description='Available commands',
        dest='command',
        help='Command help',
        required=True
    )
    
    # 'add' subcommand
    parser_add = subparsers.add_parser('add', 
                                        help='Add a new task')
    parser_add.add_argument('description', 
                            help='Task description')
    parser_add.add_argument('-p', '--priority',
                            choices=['low', 'medium', 'high'],
                            default='medium',
                            help='Task priority (default: %(default)s)')
    
    # 'list' subcommand
    parser_list = subparsers.add_parser('list', 
                                         help='List tasks')
    parser_list.add_argument('-a', '--all',
                             action='store_true',
                             help='Show completed tasks too')
    parser_list.add_argument('--format',
                             choices=['simple', 'detailed', 'json'],
                             default='simple',
                             help='Output format')
    
    # 'complete' subcommand
    parser_complete = subparsers.add_parser('complete',
                                            help='Mark task as complete')
    parser_complete.add_argument('task_id',
                                 type=int,
                                 help='Task ID to complete')
    
    # 'stats' subcommand
    parser_stats = subparsers.add_parser('stats',
                                         help='Show statistics')
    
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    # Initialize task manager
    tm = TaskManager(args.db)
    
    # Execute based on subcommand
    if args.command == 'add':
        task_id = tm.add_task(args.description, args.priority)
        print(f"✓ Task added with ID: {task_id}")
    
    elif args.command == 'list':
        tasks = tm.list_tasks(show_completed=args.all)
        
        if not tasks:
            print("No tasks found")
            return
        
        if args.format == 'json':
            print(json.dumps(tasks, indent=2))
        elif args.format == 'detailed':
            for task in tasks:
                status = "✓" if task['completed'] else "○"
                print(f"{status} [{task['id']}] {task['description']}")
                print(f"  Priority: {task['priority']}")
                print(f"  Created: {task['created']}")
                if task['completed']:
                    print(f"  Completed: {task.get('completed_at', 'Unknown')}")
                print()
        else:  # simple format
            for task in tasks:
                status = "✓" if task['completed'] else "○"
                priority_symbol = {'low': '↓', 'medium': '-', 'high': '↑'}
                p = priority_symbol[task['priority']]
                print(f"{status} [{task['id']}] {p} {task['description']}")
    
    elif args.command == 'complete':
        if tm.complete_task(args.task_id):
            print(f"✓ Task {args.task_id} completed")
        else:
            print(f"✗ Task {args.task_id} not found")
            parser.exit(1)
    
    elif args.command == 'stats':
        total = len(tm.tasks)
        completed = sum(1 for t in tm.tasks if t['completed'])
        pending = total - completed
        
        print("Task Statistics")
        print("=" * 30)
        print(f"Total tasks:     {total}")
        print(f"Completed:       {completed}")
        print(f"Pending:         {pending}")
        if total > 0:
            print(f"Completion rate: {completed/total*100:.1f}%")

if __name__ == "__main__":
    main()
```

Usage examples:
```bash
$ task add "Write documentation" --priority high
✓ Task added with ID: 1

$ task add "Review pull request"
✓ Task added with ID: 2

$ task list
○ [1] ↑ Write documentation
○ [2] - Review pull request

$ task complete 1
✓ Task 1 completed

$ task list --all --format detailed
✓ [1] Write documentation
  Priority: high
  Created: 2024-01-20T10:30:00
  Completed: 2024-01-20T11:45:00

○ [2] Review pull request
  Priority: medium
  Created: 2024-01-20T10:31:00

$ task stats
Task Statistics
==============================
Total tasks:     2
Completed:       1
Pending:         1
Completion rate: 50.0%
```

### Configuration Files

Professional CLIs often support configuration files to set defaults:

```python
import argparse
import configparser
from pathlib import Path

def load_config(config_file='~/.myapp/config.ini'):
    """Load configuration from file."""
    config = configparser.ConfigParser()
    config_path = Path(config_file).expanduser()
    
    # Default configuration
    defaults = {
        'output_format': 'json',
        'verbose': False,
        'timeout': 30,
    }
    
    if config_path.exists():
        config.read(config_path)
        # Override defaults with config file values
        if 'settings' in config:
            for key, value in config['settings'].items():
                if key in defaults:
                    # Convert strings to appropriate types
                    if isinstance(defaults[key], bool):
                        defaults[key] = config.getboolean('settings', key)
                    elif isinstance(defaults[key], int):
                        defaults[key] = config.getint('settings', key)
                    else:
                        defaults[key] = value
    
    return defaults

def create_parser(defaults):
    """Create parser with defaults from config."""
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--format',
                        default=defaults['output_format'],
                        help=f"Output format (default: {defaults['output_format']})")
    
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        default=defaults['verbose'],
                        help='Verbose output')
    
    parser.add_argument('--timeout',
                        type=int,
                        default=defaults['timeout'],
                        help=f"Timeout in seconds (default: {defaults['timeout']})")
    
    # Allow overriding config file location
    parser.add_argument('--config',
                        help='Configuration file path')
    
    return parser

def main():
    # First, parse just the config argument
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument('--config')
    pre_args, remaining = pre_parser.parse_known_args()
    
    # Load config
    config_file = pre_args.config or '~/.myapp/config.ini'
    defaults = load_config(config_file)
    
    # Create main parser with defaults
    parser = create_parser(defaults)
    args = parser.parse_args(remaining)
    
    # Now args contains values from: command line > config file > defaults
    print(f"Format: {args.format}")
    print(f"Verbose: {args.verbose}")
    print(f"Timeout: {args.timeout}")
```

### Environment Variables

Another way to configure CLIs is through environment variables:

```python
import os
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    
    # Check environment variables for defaults
    parser.add_argument('--api-key',
                        default=os.environ.get('MYAPP_API_KEY'),
                        help='API key (or set MYAPP_API_KEY env var)')
    
    parser.add_argument('--endpoint',
                        default=os.environ.get('MYAPP_ENDPOINT', 
                                              'https://api.example.com'),
                        help='API endpoint URL')
    
    parser.add_argument('--debug',
                        action='store_true',
                        default=os.environ.get('MYAPP_DEBUG', '').lower() == 'true',
                        help='Enable debug mode')
    
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.api_key:
        parser.error("API key required. Use --api-key or set MYAPP_API_KEY")
    
    print(f"Using endpoint: {args.endpoint}")
    if args.debug:
        print(f"API Key: {args.api_key[:4]}...")  # Show only first 4 chars
```

---

## Real-World Patterns

### Pattern 1: Verbose Logging Levels

```python
import argparse
import logging

def setup_logging(verbosity):
    """Configure logging based on verbosity level."""
    levels = [
        logging.WARNING,  # 0: Default
        logging.INFO,     # 1: -v
        logging.DEBUG,    # 2: -vv
    ]
    
    level = levels[min(verbosity, len(levels) - 1)]
    
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        if verbosity > 1 else '%(levelname)s: %(message)s'
    )

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose',
                        action='count',
                        default=0,
                        help='Increase verbosity (-vvv for maximum)')
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    setup_logging(args.verbose)
    
    # Now use logging throughout your application
    logging.debug("Debug message (only with -vv)")
    logging.info("Info message (only with -v)")
    logging.warning("Warning message (always shown)")
```

### Pattern 2: Dry Run Mode

```python
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', help='Files to process')
    parser.add_argument('--dry-run', '-n',
                        action='store_true',
                        help="Show what would be done without doing it")
    return parser

def process_file(filepath, dry_run=False):
    if dry_run:
        print(f"[DRY RUN] Would process: {filepath}")
    else:
        print(f"Processing: {filepath}")
        # Actual processing here
        with open(filepath, 'r') as f:
            # Do something
            pass

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if args.dry_run:
        print("DRY RUN MODE - No changes will be made")
        print("-" * 40)
    
    for filepath in args.files:
        process_file(filepath, args.dry_run)
```

### Pattern 3: Interactive Confirmation

```python
import argparse

def confirm(message="Continue?"):
    """Ask for user confirmation."""
    while True:
        response = input(f"{message} [y/N]: ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no', '']:
            return False
        else:
            print("Please enter 'y' or 'n'")

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', '-f',
                        action='store_true',
                        help='Skip confirmation prompts')
    parser.add_argument('--delete',
                        action='store_true',
                        help='Delete files')
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    if args.delete:
        if args.force or confirm("Really delete files?"):
            print("Deleting files...")
            # Deletion logic here
        else:
            print("Operation cancelled")
```

### Pattern 4: Progress Indicators

```python
import argparse
import time
from pathlib import Path

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', type=Path)
    parser.add_argument('--quiet', '-q',
                        action='store_true',
                        help='Suppress progress output')
    return parser

def process_files_with_progress(files, quiet=False):
    total = len(files)
    
    for i, filepath in enumerate(files, 1):
        if not quiet:
            # Show progress
            percent = (i / total) * 100
            bar_length = 40
            filled = int(bar_length * i // total)
            bar = '█' * filled + '░' * (bar_length - filled)
            print(f'\rProgress: [{bar}] {percent:.1f}% ({i}/{total})', 
                  end='', flush=True)
        
        # Simulate processing
        time.sleep(0.1)
        # Actual processing here
    
    if not quiet:
        print()  # New line after progress bar
        print("✓ Processing complete!")

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    process_files_with_progress(args.files, args.quiet)

if __name__ == "__main__":
    main()
```

### Pattern 5: Output Formats

```python
import argparse
import json
import csv
import sys
from io import StringIO

def output_json(data, file=sys.stdout):
    json.dump(data, file, indent=2)
    file.write('\n')

def output_csv(data, file=sys.stdout):
    if not data:
        return
    
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

def output_table(data, file=sys.stdout):
    if not data:
        return
    
    # Calculate column widths
    headers = list(data[0].keys())
    widths = {h: len(h) for h in headers}
    
    for row in data:
        for key, value in row.items():
            widths[key] = max(widths[key], len(str(value)))
    
    # Print header
    header_line = ' | '.join(h.ljust(widths[h]) for h in headers)
    file.write(header_line + '\n')
    file.write('-' * len(header_line) + '\n')
    
    # Print rows
    for row in data:
        line = ' | '.join(str(row[h]).ljust(widths[h]) for h in headers)
        file.write(line + '\n')

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--format', '-f',
                        choices=['json', 'csv', 'table'],
                        default='table',
                        help='Output format')
    parser.add_argument('--output', '-o',
                        type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file (default: stdout)')
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    # Sample data
    data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
    ]
    
    # Output in requested format
    if args.format == 'json':
        output_json(data, args.output)
    elif args.format == 'csv':
        output_csv(data, args.output)
    else:  # table
        output_table(data, args.output)
    
    # Close file if not stdout
    if args.output != sys.stdout:
        args.output.close()
```