---
layout: page
title: Linux Shell Introduction
---

# Working with a Linux Environment

## Why Learn the Shell?

In the field of datascience, you'll frequently work with datasets, run Python scripts, and manage files. The shell is your Swiss Army knife for these tasks. With a "bit" of knowledge and practice, it can become faster than clicking through folders, more reliable than big and fancy mordern apps, and essential for remote servers. It can make you feel like a wizard.

## Setting Up Your Environment

### Windows: WSL (Windows Subsystem for Linux)
1. Open PowerShell as Administrator
2. Run: `wsl --install`
3. Restart your computer
4. Set up Ubuntu username/password
5. Access via "Ubuntu" app, the windows terminal or the VS Code terminal

### Mac: Terminal
- Already installed! Find it in Applications → Utilities
- Or press `Cmd + Space`, type "terminal"

### ChromeOS: Linux Environment
- Settings → Advanced → Developers → Linux development environment
- Turn on and follow setup

## Essential Commands

### Navigation
```bash
pwd          # Where am I?
ls           # What's here?
ls -la       # Detailed view
cd folder    # Go into folder
cd ..        # Go up one level
cd ~         # Go home
```

### File Operations
```bash
mkdir data          # Create folder
cp file.csv backup/ # Copy file
mv old.txt new.txt  # Rename/move
rm file.txt         # Delete file
rm -rf folder/      # Delete folder (careful!)
```

### File Viewing
```bash
cat data.csv        # Show entire file
head -10 data.csv   # First 10 lines
tail -20 log.txt    # Last 20 lines
less large_file.txt # Browse large files
```

### Text Processing
```bash
grep "GDP" report.txt    # Find lines containing "GDP"
wc -l data.csv          # Count lines
sort numbers.txt        # Sort alphabetically
sort -n numbers.txt     # Sort numerically
```

### File Management
```bash
find . -name "*.py"     # Find all Python files
du -sh *               # Check folder sizes
chmod +x script.py     # Make script executable
```

## Package Management

### Linux (apt)
```bash
sudo apt update                # Update package list
sudo apt install python3-pip  # Install pip
sudo apt install sqlite3      # Install SQLite
```

### Mac (brew)
```bash
# First install Homebrew from brew.sh
brew install python3
brew install sqlite3
```

## Quick SQLite Recap

```bash
# Create/open database
sqlite3 mydata.db

# Basic SQL commands
.tables              # Show tables
.schema table_name   # Show table structure
.quit               # Exit

# Import CSV
.mode csv
.import data.csv mytable
```


## Pro Tips

- Use `Tab` for auto-completion
- Use `↑` arrow to recall previous commands
- `Ctrl+C` stops running commands
- `clear` cleans up your terminal
- `history` shows your command history

