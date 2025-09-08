---
layout: page
title: Linux Shell Introduction
class_number: 1
---

# Working with a Linux Environment

Welcome to Advanced Programming! In this first class, we'll set up a Linux environment for our coursework. If you're using Mac, you can skip the setup section and jump straight to learning the shell commands.

## Why Learn the Shell?

The command line (terminal/shell) is an essential tool for programmers and data scientists. Here's why:

- **Speed**: Once you know a few commands, you'll navigate and manipulate files faster than with a graphical interface
- **Automation**: Repetitive tasks can be scripted and run instantly
- **Remote Access**: Most servers don't have graphical interfaces. The shell is your only option
- **Universal**: These skills transfer across Linux, Mac, and cloud platforms
- **Power**: Some operations are only possible through the command line


## Setting Up Your Linux Environment (or equivalent)

### Windows Users: Installing WSL (Windows Subsystem for Linux)

WSL lets you run a real Linux environment directly on Windows. No virtual machine needed!  
Many programmers should this option now that it is reliable. 
It lets you keep your windows as you like it but gives you the convenience of Linux for your programming tasks. 
You also get to keep the Windows native VSCode.

**Quick Setup (5–10 minutes):**
1. Open PowerShell as Administrator (right-click → "Run as administrator")
2. Run this command: `wsl --install` (this will install install the latest Ubuntu distribution)
3. Restart your computer when prompted
4. After restart, Ubuntu will open automatically
5. Create a username and password (remember these!)
6. Access Ubuntu through:
   - The "Ubuntu" app from your Start menu
   - Windows Terminal (recommended - [install from Microsoft Store](https://aka.ms/terminal))
   - VS Code's integrated terminal
7. Set up VS Code for WSL development:  [see here](https://code.visualstudio.com/docs/remote/wsl)
   - Use the Windows native Vscode with the linux environment (combine the best of both world)
   - Install the extensions WSL in vscode
   - Press Ctrl+Shift+P
   - Type "WSL: Connect to WSL" and select it

📚 **Helpful Resources:**
- [Official WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)
- [WSL Best Practices](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)

#### Understanding Your New Linux Environment

**Important:** WSL creates a separate Linux world within Windows. Think of it as having two computers in one:

- **Your Linux Home**: When you open Ubuntu, you start in `/home/yourusername/`
- **Your Windows Files**: Accessible at `/mnt/c/` (C: drive), `/mnt/d/` (D: drive), etc.
- **Best Practice**: Keep your programming projects in the Linux filesystem for better performance

**Quick tip:** To open your current Linux folder in Windows Explorer, type: `explorer.exe .`

### Git Bash

If you are using Windows but can't or don't want to use WSL, you can use git bash ([Install here](https://git-scm.com/downloads/win)). This is a linux shell available on windows. 

### Mac Users:

Mac offers a clean programming experience with its Unix-based foundation, eliminating the need for a separate Linux environment. The terminal is nearly identical to Linux, making it ideal for Python and SQL development.

Your Terminal is already installed and ready:
- Find it in: Applications → Utilities → Terminal
- Or press `Cmd + Space`, type "terminal," and hit Enter
- Consider installing [iTerm2](https://iterm2.com/) for a better terminal experience

### ChromeOS Users: Enable Linux

1. Go to Settings → Advanced → Developers
2. Turn on "Linux development environment"
3. Follow the setup wizard (takes about 5 minutes)
4. Access via the Terminal app in your launcher
5. [More info with this link](https://support.google.com/chromebook/answer/9145439?hl=en


## Understanding Your File System

### The HOME Directory

Every user has a special directory called HOME. This is your personal space where you can create files and folders.

```bash
# Your HOME directory is represented by ~
cd ~                # Go to your home directory
echo $HOME          # Display the path to your home
                   # Output: /home/yourusername (Linux)
                   #         /Users/yourusername (Mac)

pwd                # When you first open terminal, you're usually here
                   # Output: /home/yourusername

# Common folders in your HOME
ls ~               # You might see: Documents, Downloads, Desktop, etc.

# These are equivalent:
cd ~               # Go home using tilde
cd $HOME           # Go home using the HOME variable
cd /home/username  # Go home using absolute path (Linux)
cd                 # Just cd with no arguments also goes home!
```

**Why is HOME important?**
- It's where your personal files live
- You have full control here (can create, delete, modify anything)
- Your settings and configurations are stored here
- It's your starting point when you open a terminal

### Absolute vs Relative Paths

```bash
# Absolute paths start with / (the root)
cd /home/username/projects    # Always works from anywhere
ls /usr/bin                   # Lists system programs

# Relative paths start from where you are
cd projects                   # Enter projects folder from current location
cd ../Documents              # Go up one level, then into Documents

# Special path shortcuts
.                            # Current directory
..                           # Parent directory (one level up)
~                            # Your home directory
-                            # Previous directory you were in
```

## Essential Shell Commands


### Navigation—Moving Around

```bash
pwd                 # Print Working Directory - shows where you are
                   # Example output: /home/username/projects

ls                  # List - shows files and folders in current directory
ls -l              # Long format - shows size, date, etc.
ls -la             # Shows hidden files too (files starting with .)
ls ~/Documents     # List files in a specific folder

cd projects        # Change Directory - enter the 'projects' folder
cd ..              # Go up one level (parent directory)
cd ~               # Go to your home directory
cd /               # Go to root directory (top of filesystem)
cd -               # Go back to previous directory
```

### File Operations—Creating and Managing Files

```bash
# Creating
mkdir my_project        # Make Directory - create a new folder
mkdir -p data/raw      # Create nested folders (data and raw inside it)
touch script.py        # Create an empty file
echo "Hello" > hi.txt  # Create file with content

# Copying
cp file.txt backup.txt           # Copy file to new name
cp file.txt ~/Documents/         # Copy file to another location
cp -r project/ project_backup/   # Copy entire folder (-r = recursive)

# Moving and Renaming
mv old_name.txt new_name.txt    # Rename a file
mv file.txt ~/Desktop/           # Move file to Desktop
mv *.csv data/                  # Move all CSV files to data folder

# Deleting (⚠️ Be careful - no recycle bin!)
rm file.txt                     # Remove file
rm -i important.txt             # Interactive - asks for confirmation
rmdir empty_folder/             # Remove empty directory only
rm -r folder_with_files/        # Remove folder and everything inside
rm -rf folder/                  # Force remove (use with extreme caution!)
```

### Viewing File Contents

```bash
cat file.txt              # Display entire file
cat file1.txt file2.txt   # Display multiple files

echo "Some text"          # Print text to screen
echo "New line" >> log.txt # Append text to file

less large_file.txt       # View file page by page
                         # Use arrows to navigate, 'q' to quit
                         # '/' to search, 'n' for next match

head data.csv            # Show first 10 lines
head -n 20 data.csv      # Show first 20 lines

tail log.txt             # Show last 10 lines
tail -n 50 log.txt       # Show last 50 lines
tail -f log.txt          # Follow file as it grows (great for logs)
```

### Finding and Searching

```bash
find . -name "*.py"           # Find all Python files from current directory
find ~/projects -name "test*" # Find files starting with "test"

grep "error" log.txt          # Find lines containing "error"
grep -i "ERROR" log.txt       # Case-insensitive search
grep -n "TODO" script.py      # Show line numbers
grep -r "import" .            # Search recursively in all files
```

### Useful Information Commands

```bash
wc file.txt              # Word Count - shows lines, words, characters
wc -l data.csv          # Count lines only (useful for CSV rows)

du -sh *                # Disk Usage - show size of files/folders
du -h --max-depth=1     # Show size of immediate subdirectories

which python3           # Show where a program is installed
whoami                  # Show your username
date                    # Show current date and time
```

## System Package Management

Package managers are like app stores for your command line. They install, update, and manage software at the system level. These are for installing programs like Python, Git, databases, etc.

### Linux (Ubuntu/Debian) - APT

APT (Advanced Package Tool) manages software on Ubuntu and Debian-based systems.

```bash
# Update package information (always do this first!)
sudo apt update

# Install packages
sudo apt install python3          # Python interpreter
sudo apt install python3-pip      # Python package manager
sudo apt install python3-venv     # Python virtual environments

# Check Python versions
python3 --version          # Should show Python 3.x.x
python --version           # Might not work or show Python 2.x

# Check what's already installed
which python3              # Shows path: /usr/bin/python3
which pip3                # Might show nothing if pip not installed

sudo apt install git              # Version control
sudo apt install curl             # Download files from internet
sudo apt install sqlite3          # SQLite database
sudo apt install build-essential  # Compilers and development tools


# Upgrade installed packages
sudo apt upgrade                  # Upgrade all packages
sudo apt upgrade package-name     # Upgrade specific package

# Remove packages
sudo apt remove package-name      # Remove package
sudo apt autoremove              # Remove unused dependencies
```

**What does `sudo` mean?** 
- Super User DO - runs commands with administrator privileges
- Required for system-wide changes like installing software
- Will ask for your password

📚 **APT Resources:**
- [Ubuntu Package Search](https://packages.ubuntu.com/)
- [APT User's Guide](https://www.debian.org/doc/manuals/apt-guide/index.en.html)

### Mac - Homebrew

Homebrew is the most popular package manager for Mac.

```bash
# First, install Homebrew (if not already installed)
# Visit https://brew.sh for the latest command, or run:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Basic commands
brew update                    # Update Homebrew itself
brew upgrade                   # Upgrade all packages
brew install python3          # Install Python 3
brew install git              # Install Git
brew install sqlite           # Install SQLite
brew install node             # Install Node.js

# Search and info
brew search mysql             # Search for packages
brew info python3             # Show package details
brew list                     # Show installed packages

# Maintenance
brew cleanup                  # Remove old versions
brew doctor                   # Check for issues
```

📚 **Homebrew Resources:**
- [Homebrew Documentation](https://docs.brew.sh/)
- [Homebrew Formulae (packages)](https://formulae.brew.sh/)


## SQLite Quick Start

SQLite has its own command-line interface, separate from your regular shell.

### Understanding Two Different Command Lines

```bash
# Regular shell prompt (where you type Linux commands)
username@computer:~$              # This is your normal shell
$ ls                              # Shell commands work here
$ cd projects                     # You can navigate directories

# SQLite prompt (a different program with its own commands)
username@computer:~$ sqlite3 mydb.db    # Start SQLite
sqlite>                                  # Now you're in SQLite!
sqlite> .tables                         # SQLite commands start with .
sqlite> SELECT * FROM users;            # SQL queries work here
sqlite> ls                              # This won't work! It's not a shell
```

**Key Difference:** 
- In the shell, you work with files and run programs
- In SQLite, you work with databases and run SQL queries
- Commands starting with `.` are SQLite-specific
- SQL statements (SELECT, CREATE, INSERT) work in SQLite
- To exit SQLite and return to shell: `.quit`

### Basic SQLite Operations

```bash
# From your regular shell, create or open a database
sqlite3 mydatabase.db

# Now you're in SQLite (notice the prompt change to sqlite>)
```

Once inside SQLite:
```sql
-- SQLite specific commands (start with a dot)
.help                  -- Show all commands
.tables               -- List all tables
.schema tablename     -- Show table structure
.headers on           -- Show column names in query results
.mode column          -- Pretty-print results in columns
.quit                 -- Exit SQLite and return to shell

-- Create a table
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade REAL
);

-- Insert data
INSERT INTO students (name, age, grade) VALUES ('Alice', 20, 85.5);
INSERT INTO students (name, age, grade) VALUES ('Bob', 21, 92.0);

-- Query data
SELECT * FROM students;
SELECT name, grade FROM students WHERE age > 20;

-- Import CSV data
.mode csv
.import data.csv mytable
```

**Remember:** 
- SQL commands end with semicolon `;`
- SQLite commands start with dot `.`
- SQL is not case-sensitive, but UPPERCASE is convention
- To go back to your shell, type `.quit`

📚 **SQLite Resources:**
- [SQLite Command Line Documentation](https://sqlite.org/cli.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [SQL in 10 Minutes](https://www.sqlitetutorial.net/sql-in-ten-minutes/)

## Pro Tips for Terminal Productivity

### Essential Shortcuts

- **Tab**: Auto-complete file names and commands (your best friend!)
- **↑ / ↓**: Navigate through command history
- **Ctrl + C**: Stop a running command
- **Ctrl + L** or `clear`: Clear the terminal screen
- **Ctrl + A**: Jump to beginning of line
- **Ctrl + E**: Jump to end of line
- **Ctrl + R**: Search command history (super useful!)
- **Ctrl + W**: Delete the last word (also beneficial)

### Time-Saving Tricks

```bash
# Use wildcards
*.txt           # All .txt files
data?.csv       # data1.csv, data2.csv, etc.
[0-9]*          # Files starting with a number

# Chain commands
mkdir project && cd project    # Create and enter directory
ls -la | less                  # Pipe output to less for viewing

# Command history
history              # Show all previous commands
history | grep git   # Find all git commands you've used
!523                # Run command #523 from history
!!                  # Run the last command again
```

### Getting Help

```bash
man ls              # Manual page for ls command (press 'q' to quit)
ls --help           # Quick help for most commands
which python3       # Find where a program is installed
type cd            # Check if something is a command or alias
```


## `$OLDPWD` - Previous Directory
Your previous working directory (where `cd -` takes you)

```bash
cd /home/user/projects
cd /var/log
cp $OLDPWD/myfile.txt .    # Copies from /home/user/projects
ls $OLDPWD                 # Lists /home/user/projects
```

## `$_` - Last Argument
The last argument of the previous command

```bash
mkdir /very/long/path/to/new-project
cd $_                      # Goes to /very/long/path/to/new-project

touch important-file.txt
vim $_                     # Opens important-file.txt
```

## `!!` - Last Command
Entire previous command

```bash
apt install docker
sudo !!                   # Runs: sudo apt install docker

rm important.txt
!!                        # Runs: rm important.txt again
```


📚 **Want to Learn More?**
- [The Linux Command Line (free book)](https://linuxcommand.org/tlcl.php)
- [Linux Journey (interactive tutorial)](https://linuxjourney.com/)
- [Explain Shell (breaks down commands)](https://explainshell.com/)
- [SQLite Browser (GUI for SQLite)](https://sqlitebrowser.org/)

