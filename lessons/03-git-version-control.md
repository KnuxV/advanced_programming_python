---
layout: page
title: Git Version Control
class_number: 3
---


# Git Version Control: From GUI to Command Line

You already know GitHub Desktop. This class introduces command-line Git, which provides more control and works in environments where GUIs aren't available, such as remote servers.

## Why Learn Command-Line Git

### Industry Context

According to the 2024 Stack Overflow Developer Survey:
- 96% of professional developers use version control systems
- Git is the dominant system across the industry
- Command-line proficiency is expected in most development roles
- Remote server administration requires terminal-based tools

In professional development environments, you'll encounter situations where:
- You need to SSH into a server to deploy or debug code
- GUI tools aren't available or practical
- You need to automate Git operations through scripts
- You need to perform complex operations not available in GUI tools

### Daily Development Workflow

A typical developer's day involves:
- Synchronizing code with team members across different time zones
- Creating focused commits that document specific changes
- Reviewing code changes before integration
- Managing multiple versions of code simultaneously
- Resolving conflicts when multiple people edit the same files

## Core Git Concepts

### Understanding the Git Architecture

Git manages your code through three main areas on your local machine, plus the remote repository:

#### Working Directory
The working directory is simply the folder on your computer where your project files exist. When you edit a file in your text editor, you're modifying files in the working directory. Git monitors this directory for changes but doesn't automatically save anything.

#### Staging Area (Index)
The staging area is a preparation zone between your working directory and the repository. When you've made changes you want to save, you explicitly add them to the staging area. This allows you to control exactly what changes go into each commit. You might edit five files but only stage three of them for a particular commit if only those three are related to the same feature.

#### Local Repository
The local repository is the complete history of your project stored in the `.git` folder. When you commit, you're taking everything in the staging area and saving it as a permanent snapshot in the local repository. Each commit has a unique identifier and includes information about what changed, who made the change, and when it occurred.

#### Remote Repository
The remote repository is a copy of your repository hosted on a server (like GitHub). It serves as a central synchronization point for your team. You push your local commits to the remote and pull other people's commits from it.

```
Working Directory → Staging Area → Local Repository → Remote Repository
     (edit)           (git add)      (git commit)       (git push)
```

### How Git Tracks Changes

Git doesn't store copies of every file in every commit. Instead, it stores:
1. The initial version of each file
2. The differences (deltas) between versions
3. Metadata about who made changes and when

This makes Git efficient even for large projects with long histories.

### The Commit: Git's Fundamental Unit

A commit represents a specific point in your project's history. Each commit contains:
- A unique SHA-1 hash identifier (like `a3f8d92`)
- The author's name and email
- A timestamp
- A commit message describing the change
- A pointer to the previous commit (its parent)
- The actual changes made to files

Commits form a chain, creating your project's history. You can move between any commits to see your project at different points in time.

## Setting Up Git

### Initial Configuration

First, configure Git with your identity. This information will be attached to your commits:

```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set the default branch name to 'main'
git config --global init.defaultBranch main

# Set your preferred text editor
git config --global core.editor "micro"

# View your configuration
git config --list
```

The `--global` flag means these settings apply to all repositories on your computer. You can override them for specific repositories by omitting the flag.

### SSH Authentication Setup

SSH (Secure Shell) provides a secure way to connect to GitHub without entering your password repeatedly. Here's how it works:

1. You generate a pair of cryptographic keys: one private (stays on your computer) and one public (shared with GitHub)
2. When you connect to GitHub, it uses these keys to verify your identity

```bash
# Generate an SSH key pair
ssh-keygen -t ed25519 -C "your.email@example.com"

# When prompted for a passphrase, you can press Enter for no passphrase
# or add one for extra security

# Start the SSH agent (manages your keys)
eval "$(ssh-agent -s)"

# Add your private key to the agent
ssh-add ~/.ssh/id_ed25519

# Display your public key
cat ~/.ssh/id_ed25519.pub

# Copy the output and add it to GitHub:
# GitHub.com → Settings → SSH and GPG keys → New SSH key

# Test the connection
ssh -T git@github.com
```

## Live Coding Session: Creating Your First Repository

We'll create a project together to understand the basic workflow.

### Step 1: Initialize a Repository

```bash
# Create a new directory for our project
mkdir python-calculator
cd python-calculator

# Initialize Git in this directory
git init

# Let's see what Git created
ls -la
```

The `git init` command creates a hidden `.git` folder that contains all of Git's tracking information. This folder is the local repository.

### Step 2: Create and Track Files

```bash
# Create a README file
echo "# Python Calculator" > README.md
echo "A simple calculator implementation" >> README.md

# Check Git's status
git status
```

Git reports that README.md is "untracked" - it sees the file but isn't managing it yet.

```bash
# Add the file to the staging area
git add README.md

# Check status again
git status
```

The file is now staged (shown in green), ready to be committed.

### Step 3: Make Your First Commit

```bash
# Create a commit with a descriptive message
git commit -m "Initial commit: Add project README"

# View the commit history
git log
```

The commit is now permanently stored in your local repository with a unique identifier.

### Step 4: Create the Calculator

```bash
# Create the calculator file using a here document
cat > calculator.py << 'EOF'
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
EOF
```

Note about `EOF`: This is called a "here document" in bash. Everything between `<< 'EOF'` and `EOF` is written to the file. EOF stands for "End Of File" but you could use any marker. The single quotes around 'EOF' prevent variable expansion in the content.

```bash
# See what changed
git status
git diff

# Stage and commit the calculator
git add calculator.py
git commit -m "Add basic calculator functions"

# View the updated history
git log --oneline
```

### Step 5: Connecting to GitHub

A remote repository is a version of your project hosted on a server. GitHub is one service that hosts Git repositories. The remote serves several purposes:
- Backup of your code
- Collaboration point for your team
- Public showcase of your work
- Deployment source for production systems

There are two common workflows for connecting local and remote repositories:

#### Method 1: Start Locally, Then Connect to GitHub

This is what we just did - create a local repository first, then connect it to GitHub:

```bash
# First, create a repository on GitHub.com through the web interface
# Important: Do NOT initialize with README, .gitignore, or license

# Add the GitHub repository as a remote named 'origin'
git remote add origin git@github.com:yourusername/python-calculator.git

# View configured remotes
git remote -v

# Push your commits to GitHub
git push -u origin main
```

The `-u` flag in `git push -u origin main` sets up tracking between your local `main` branch and the remote `main` branch. After this, you can simply use `git push` and `git pull` without specifying the remote and branch.

#### Method 2: Start on GitHub, Then Clone Locally

This method is often simpler, especially for new projects:

```bash
# 1. Create a repository on GitHub.com through the web interface
#    - You can initialize with README, .gitignore, and license
#    - GitHub provides templates for different languages

# 2. Clone the repository to your computer
git clone git@github.com:yourusername/project-name.git

# 3. Enter the project directory
cd project-name

# 4. Start working - you're already connected to GitHub
# The remote 'origin' is automatically configured
```

When you clone a repository:
- Git automatically sets up the remote named 'origin'
- The tracking relationship is already configured
- You can immediately use `git push` and `git pull`

#### Which Method to Use?

**Start locally** when:
- You already have code written
- You're converting an existing project to use Git
- You want full control over initial repository structure

**Start on GitHub** when:
- Beginning a new project
- You want GitHub's templates (.gitignore, license, README)
- Multiple people need immediate access
- You want the simpler setup process

Both methods achieve the same result: a local repository connected to GitHub.

## Understanding Branches

### What Are Branches

A branch is an independent line of development. Think of your project's history as a tree:
- The trunk is your main branch
- Branches split off to develop features
- Branches can be merged back into the trunk

Every repository starts with one branch (usually called `main` or `master`). When you create a new branch, you're creating a new pointer to a specific commit. Changes on the branch don't affect other branches until you explicitly merge them.

### Why Use Branches

Branches solve several problems:

1. **Isolation**: Develop features without affecting stable code
2. **Collaboration**: Multiple people can work simultaneously without interference
3. **Experimentation**: Try ideas without commitment
4. **Organization**: Group related commits together
5. **Code Review**: Changes can be reviewed before merging

### Working with Branches

```bash
# View all branches
git branch

# Create a new branch
git branch feature-tests

# Switch to the new branch
git checkout feature-tests

# Or create and switch in one command
git checkout -b feature-tests

# Make changes on the branch
cat > test_calculator.py << 'EOF'
import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_divide():
    assert calculator.divide(10, 2) == 5
    try:
        calculator.divide(10, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

if __name__ == "__main__":
    test_add()
    test_divide()
    print("All tests passed")
EOF

# Commit on the branch
git add test_calculator.py
git commit -m "Add unit tests for calculator"

# Switch back to main
git checkout main

# Merge the feature branch
git merge feature-tests

# Delete the branch after merging
git branch -d feature-tests
```

## Understanding Merge Conflicts

### What Causes Conflicts

A merge conflict occurs when Git cannot automatically combine changes. This happens when:
- Two branches modify the same line of a file
- One branch deletes a file that another branch modifies
- Files are renamed differently in different branches

### How Git Marks Conflicts

When a conflict occurs, Git modifies the affected files to show both versions:

```
<<<<<<< HEAD
    your version of the code
=======
    their version of the code
>>>>>>> branch-name
```

- `HEAD` refers to your current branch
- The other marker shows the branch you're merging

### Resolving Conflicts

1. Open the conflicted file
2. Decide which version to keep (or combine them)
3. Remove the conflict markers
4. Stage the resolved file
5. Complete the merge with a commit

```bash
# Example of resolving a conflict
# After attempting a merge that conflicts:

# See which files have conflicts
git status

# Edit the file to resolve conflicts
micro conflicted_file.py

# After editing, mark as resolved
git add conflicted_file.py

# Complete the merge
git commit -m "Merge feature branch and resolve conflicts"
```

## Pull Requests and Code Review

### The Pull Request Process

A pull request (PR) is a GitHub feature that facilitates code review. The process:

1. You push your branch to GitHub
2. You open a pull request to propose merging your branch
3. Team members review your code
4. Discussions and changes happen
5. Once approved, the branch is merged

This process ensures:
- Code quality through peer review
- Knowledge sharing across the team
- Documentation of why changes were made
- Opportunity to catch bugs before they reach production

### Creating a Pull Request

```bash
# Push your feature branch to GitHub
git push origin feature-branch

# GitHub will display a message with a link to create a PR
# Or navigate to your repository on GitHub and click "Pull requests"
```

## Essential Git Commands Reference

### Information Commands

```bash
git status              # Show working directory status
git log                 # Show commit history
git log --oneline      # Compact history view
git diff               # Show unstaged changes
git diff --staged      # Show staged changes
git branch             # List branches
git remote -v          # Show remote repositories
```

### Basic Workflow Commands

```bash
git add <file>         # Stage specific file
git add .              # Stage all changes
git commit -m "msg"    # Commit staged changes
git push               # Push to remote repository
git pull               # Fetch and merge from remote
git fetch              # Fetch without merging
```

### Branch Commands

```bash
git checkout -b <branch>    # Create and switch to branch
git checkout <branch>       # Switch to existing branch
git merge <branch>         # Merge branch into current branch
git branch -d <branch>     # Delete local branch
```

### Undoing Changes

```bash
git checkout -- <file>      # Discard working directory changes
git reset HEAD <file>       # Unstage file
git reset --soft HEAD~1     # Undo last commit, keep changes staged
git reset HEAD~1           # Undo last commit, keep changes unstaged
git reset --hard HEAD~1    # Undo last commit, discard changes
git revert <commit>        # Create new commit that undoes specific commit
```

## The .gitignore File

### Purpose

The `.gitignore` file tells Git which files to ignore. Use it for:
- Build artifacts that can be regenerated
- Dependencies that can be reinstalled
- Local configuration files
- Sensitive information like passwords
- Operating system files

### Common Python .gitignore

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/

# Testing
.coverage
.pytest_cache/
htmlcov/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment variables
.env

# Data
*.csv
*.sqlite
*.db
```

## Writing Effective Commit Messages

### Structure

A good commit message explains what changed and why. Format:

```
<type>: <summary>

[optional body]
[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code restructuring
- `test`: Test additions or changes
- `chore`: Maintenance tasks

### Examples

```bash
# Good messages
git commit -m "fix: Prevent division by zero in calculator"
git commit -m "feat: Add exponential function to calculator"
git commit -m "docs: Add usage examples to README"

# Poor messages
git commit -m "fixed bug"
git commit -m "updates"
git commit -m "wip"
```

## Practice Exercises

### Exercise 1: Basic Workflow

Create a repository for a Python project:

1. Initialize a new repository
2. Create a Python module with at least two functions
3. Make three separate commits, each adding functionality
4. Push to GitHub

### Exercise 2: Branch and Merge

Using your repository from Exercise 1:

1. Create a feature branch
2. Add a new function on the branch
3. Switch to main and modify an existing function
4. Merge the feature branch
5. Push all branches to GitHub

### Exercise 3: Collaboration Simulation

Work with a partner:

1. Person A creates a repository with initial code
2. Person B clones and adds a feature on a branch
3. Person A makes changes to the same file on main
4. Person B creates a pull request
5. Resolve any conflicts together


### Need to Temporarily Save Work

```bash
git stash                  # Save current changes
git stash list            # View stashed changes
git stash pop             # Restore changes
```


## Resources for Continued Learning

### Interactive Learning
- [Learn Git Branching](https://learngitbranching.js.org/) - Visual and interactive tutorial
- [GitHub Skills](https://skills.github.com/) - GitHub's official interactive courses

### Reference Documentation
- [Pro Git Book](https://git-scm.com/book) - Comprehensive Git reference
- [GitHub Docs](https://docs.github.com) - GitHub-specific features and workflows

### Problem Solving
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Solutions to common Git mistakes
- [Git Flight Rules](https://github.com/k88hudson/git-flight-rules) - What to do when things go wrong


---
