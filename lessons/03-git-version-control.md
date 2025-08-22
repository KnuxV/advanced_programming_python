---
layout: page
title: Git Version Control
---

# Git Version Control: From GUI to Command Line

You already know GitHub Desktop - that's great! Now let's unlock the full power of Git through the command line. While GitHub Desktop is user-friendly, the terminal gives you speed, flexibility, and works everywhere - especially on servers where GUIs don't exist.

## Why Git Matters (A Quick Refresher)

### The Problem Git Solves

Imagine working on a project without Git:
```
final_project.py
final_project_v2.py
final_project_v2_FINAL.py
final_project_v2_FINAL_ACTUALLY.py
final_project_backup_before_breaking_everything.py
final_project_THIS_ONE_WORKS.py
```

Sound familiar? Git solves this chaos by:
- **Tracking Changes**: Every edit is recorded with who, what, when, and why
- **Collaboration**: Multiple people can work on the same code without conflicts
- **Time Travel**: Revert to any previous version instantly
- **Branching**: Experiment safely without breaking working code
- **Backup**: Your code lives in multiple places (local + GitHub)

### Real-World Git Usage

**How professionals use Git daily:**
- **Morning**: Pull latest changes from team
- **Coding**: Commit progress every 30-60 minutes
- **Feature complete**: Push to GitHub, create pull request
- **Code review**: Team reviews and suggests improvements
- **Merge**: Changes integrated into main project
- **Deploy**: Tested code goes to production

**Your future employer expects you to:**
- Commit code with clear messages
- Work on feature branches
- Submit pull requests for review
- Resolve merge conflicts
- Collaborate asynchronously with global teams

## Git Fundamentals: The Mental Model

### The Three States of Git

Every file in your project exists in one of three states:

```
Working Directory          Staging Area              Repository
(Your files)              (Ready to commit)         (Saved history)
     |                          |                         |
     |  ----git add---->        |                         |
     |                          |  ---git commit--->      |
     |  <------------------git checkout---------------    |
```

1. **Working Directory**: Your actual files you're editing
2. **Staging Area**: Files marked for the next commit (snapshot)
3. **Repository**: The saved history of all your commits

### Key Concepts

**Repository (Repo)**: A folder tracked by Git (.git folder inside)
**Commit**: A snapshot of your code at a specific point in time
**Branch**: An independent line of development
**Remote**: A copy of your repo on another computer (like GitHub)
**Clone**: Download a complete copy of a remote repository
**Pull Request (PR)**: Request to merge your changes into another branch

## Setting Up Git

### Initial Configuration

```bash
# Check if Git is installed
git --version

# If not installed:
# Ubuntu/WSL: sudo apt install git
# Mac: brew install git

# Configure your identity (use your GitHub email!)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set your default branch name to 'main' (modern standard)
git config --global init.defaultBranch main

git config --global core.editor "nano"         # Simple terminal editor

# View your configuration
git config --list
```

### SSH Setup for GitHub (Recommended)

SSH lets you push to GitHub without entering your password every time.

```bash
# 1. Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your.email@example.com"
# Just press Enter for all prompts (uses defaults)

# 2. Start SSH agent
eval "$(ssh-agent -s)"

# 3. Add your key to the agent
ssh-add ~/.ssh/id_ed25519

# 4. Copy your public key
cat ~/.ssh/id_ed25519.pub
# Select and copy the output

# 5. Add to GitHub:
# - Go to GitHub.com → Settings → SSH and GPG keys
# - Click "New SSH key"
# - Paste your key and save

# 6. Test the connection
ssh -T git@github.com
# You should see: "Hi username! You've successfully authenticated..."
```

## Essential Git Commands

### Starting a New Project

```bash
# Method 1: Start locally, push to GitHub later
mkdir my-project
cd my-project
git init                    # Initialize Git in this folder
echo "# My Project" > README.md
git add README.md
git commit -m "Initial commit"

# Create repo on GitHub (via website), then:
git remote add origin git@github.com:yourusername/my-project.git
git push -u origin main     # -u sets upstream for future pushes

# Method 2: Start from GitHub (Recommended)
# Create repo on GitHub first, then:
git clone git@github.com:yourusername/my-project.git
cd my-project
# Start working!
```

### Daily Workflow Commands

```bash
# 1. Start your day - get latest changes
git pull                    # Update your local repo

# 2. Check what's happening
git status                  # See what files changed
git diff                    # See exact changes in files
git diff --staged          # See what's ready to commit

# 3. Save your work
git add file.py            # Stage specific file
git add .                  # Stage all changes (use carefully!)
git add *.py              # Stage all Python files

# 4. Commit with meaningful message
git commit -m "Add user authentication feature"
# or for longer messages:
git commit                 # Opens editor for detailed message

# 5. Share your work
git push                   # Send commits to GitHub
git push origin main       # Specify remote and branch
```

### Viewing History

```bash
# See commit history
git log                    # Full history
git log --oneline         # Compact view
git log --graph --all     # Visual branch structure
git log -3                # Last 3 commits
git log --author="Alice"  # Commits by specific person
git log --since="2 weeks ago"

# See what changed in a commit
git show                   # Show last commit
git show abc123           # Show specific commit
git diff HEAD~1           # Compare with previous commit
```

### Undoing Changes

```bash
# Discard changes in working directory
git checkout -- file.py    # Restore single file
git checkout .            # Restore all files

# Unstage files (keep changes)
git reset HEAD file.py    # Unstage single file
git reset HEAD            # Unstage everything

# Undo last commit (keep changes)
git reset --soft HEAD~1   # Undo commit, keep staged
git reset HEAD~1          # Undo commit and staging
git reset --hard HEAD~1   # ⚠️ DESTRUCTIVE: Lose all changes

# Fix last commit message
git commit --amend -m "Better commit message"

# Add forgotten file to last commit
git add forgotten_file.py
git commit --amend --no-edit
```

## Working with Branches

Branches let you work on features without affecting the main code.

### Branch Basics

```bash
# View branches
git branch                 # Local branches (* = current)
git branch -a             # All branches (including remote)

# Create and switch branches
git branch feature-login   # Create branch
git checkout feature-login # Switch to branch
# or both at once:
git checkout -b feature-login

# Work on your branch
echo "def login():" > auth.py
git add auth.py
git commit -m "Add login function"

# Switch back to main
git checkout main

# Merge your feature
git merge feature-login    # Merge into current branch

# Delete branch after merging
git branch -d feature-login # Safe delete (only if merged)
git branch -D feature-login # Force delete
```

### Remote Branches

```bash
# Push new branch to GitHub
git push -u origin feature-login

# Get remote branch from teammate
git fetch                  # Update remote info
git checkout -b feature-login origin/feature-login

# Delete remote branch
git push origin --delete feature-login
```

## Collaboration: Pull Requests

Pull Requests (PRs) are how teams review and merge code. Here's the full workflow:

### The PR Workflow

```bash
# 1. Create feature branch
git checkout -b add-search-feature

# 2. Make changes and commit
vim search.py
git add search.py
git commit -m "Implement search functionality"

# 3. Push to GitHub
git push -u origin add-search-feature

# 4. GitHub will show: "Compare & pull request" - click it!
# Or go to: https://github.com/username/repo/pulls

# 5. On GitHub:
# - Write PR description
# - Assign reviewers
# - Link related issues
# - Submit PR

# 6. After approval, merge on GitHub

# 7. Clean up locally
git checkout main
git pull                  # Get the merged changes
git branch -d add-search-feature
```

### Keeping Your Fork Updated

When contributing to other projects:

```bash
# 1. Fork on GitHub (click Fork button)

# 2. Clone your fork
git clone git@github.com:yourusername/their-project.git
cd their-project

# 3. Add original repo as upstream
git remote add upstream git@github.com:originalowner/their-project.git

# 4. Keep your fork updated
git fetch upstream        # Get latest from original
git checkout main
git merge upstream/main   # Merge into your fork
git push origin main      # Update your GitHub fork

# 5. Create PR from your fork to original
```

## Writing Good Commit Messages

### The Golden Rules

```bash
# ❌ Bad commits
git commit -m "fixed stuff"
git commit -m "asdfasdf"
git commit -m "wip"

# ✅ Good commits
git commit -m "Fix null pointer exception in user login"
git commit -m "Add password strength validation"
git commit -m "Refactor database connection to use connection pooling"
```

### Commit Message Format

```bash
# Format: <type>: <subject>
# 
# Types:
# feat: New feature
# fix: Bug fix
# docs: Documentation
# style: Formatting, missing semicolons, etc.
# refactor: Code restructuring
# test: Adding tests
# chore: Maintenance

git commit -m "feat: Add email verification for new users"
git commit -m "fix: Resolve memory leak in image processor"
git commit -m "docs: Update API documentation for v2 endpoints"
```

### Multi-line Commits (for complex changes)

```bash
git commit
# Opens editor, write:
# 
# feat: Add shopping cart functionality
# 
# - Implement cart model with add/remove methods
# - Create cart API endpoints
# - Add cart icon to navbar with item count
# - Store cart in localStorage for persistence
# 
# Closes #45
```

## Handling Merge Conflicts

Conflicts happen when two people change the same lines. Don't panic!

### Resolving Conflicts

```bash
# 1. Attempt to merge
git pull  # or git merge feature-branch

# 2. Git reports conflict
# Auto-merging file.py
# CONFLICT (content): Merge conflict in file.py

# 3. Check status
git status
# Shows: both modified: file.py

# 4. Open the conflicted file
# You'll see:
<<<<<<< HEAD
    your code here
=======
    their code here
>>>>>>> feature-branch

# 5. Edit file to resolve:
# - Remove the markers (<<<<, ====, >>>>)
# - Keep the code you want (yours, theirs, or both)
# - Save the file

# 6. Mark as resolved
git add file.py
git commit -m "Resolve merge conflict in file.py"
```

### Preventing Conflicts

```bash
# Best practices:
# 1. Pull before starting work
git pull

# 2. Commit often (smaller commits = easier merges)
# 3. Communicate with team about who's working on what
# 4. Keep branches short-lived (merge within days, not weeks)
```

## Advanced Git Commands

### Stashing - Temporary Storage

```bash
# Save work without committing
git stash                  # Stash current changes
git stash list            # See all stashes
git stash pop             # Apply and delete latest stash
git stash apply           # Apply but keep stash
git stash drop            # Delete latest stash

# Named stashes
git stash save "work in progress on login"
git stash apply stash@{1} # Apply specific stash
```

### Cherry-picking - Copy Specific Commits

```bash
# Copy a commit from another branch
git cherry-pick abc123    # Apply commit abc123 to current branch
git cherry-pick --continue # After resolving conflicts
```

### Interactive Rebase - Rewrite History

```bash
# Clean up last 3 commits before pushing
git rebase -i HEAD~3
# Editor opens, you can:
# - reorder commits
# - squash commits together
# - edit commit messages
# - drop commits

# ⚠️ Never rebase commits that are already pushed!
```

## Git Aliases - Work Faster

```bash
# Create shortcuts for common commands
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
git config --global alias.last 'log -1 HEAD'
git config --global alias.unstage 'reset HEAD --'
git config --global alias.visual '!gitk'

# Now you can use:
git st                    # Instead of git status
git co main              # Instead of git checkout main
```

## .gitignore - What Not to Track

Create `.gitignore` file in your repo root:

```bash
# Python
*.pyc
__pycache__/
venv/
.env
*.log

# Data files
*.csv
*.xlsx
data/

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Secrets - NEVER commit these!
.env
config/secrets.yml
*.key
*.pem
```

## Git GUI Tools

While we focus on command line, these tools can help visualize complex histories:

- **GitHub Desktop**: You already know this!
- **GitKraken**: Beautiful visualizations
- **SourceTree**: Free, comprehensive
- **VS Code**: Built-in Git integration
- **gitk**: Simple tool included with Git (`gitk --all`)

## Practice Exercises

### Exercise 1: Your First Repository

Create a Python calculator and track it with Git:

```bash
# 1. Create and initialize
mkdir python-calculator
cd python-calculator
git init

# 2. Create calculator
echo "def add(a, b):
    return a + b

def subtract(a, b):
    return a - b" > calculator.py

# 3. Track and commit
git add calculator.py
git commit -m "feat: Add basic calculator functions"

# 4. Add more features on a branch
git checkout -b add-multiplication
echo "
def multiply(a, b):
    return a * b" >> calculator.py
git add calculator.py
git commit -m "feat: Add multiplication function"

# 5. Merge to main
git checkout main
git merge add-multiplication

# 6. Push to GitHub
# Create repo on GitHub first, then:
git remote add origin git@github.com:yourusername/python-calculator.git
git push -u origin main
```

### Exercise 2: Contribute to Open Source

Find a project with "good first issue" labels and contribute:

1. Go to: https://github.com/topics/good-first-issue
2. Find a Python project you like
3. Fork it
4. Clone your fork
5. Create a branch for your fix
6. Make changes
7. Push and create a PR

### Exercise 3: Class Repository Contribution (EXTRA CREDIT!)

**Earn bonus points by improving our class materials!**

The class repository is at: `github.com/[your-username]/advanced-programming-class`

Your mission:
1. Fork the class repository
2. Find something to improve:
   - Fix a typo
   - Add a helpful example
   - Improve an explanation
   - Add a useful resource link
   - Create a helpful diagram
   - Add practice problems
3. Create a branch with a descriptive name
4. Make your improvements
5. Submit a pull request with:
   - Clear PR title
   - Description of what you changed and why
   - Reference to any issues (if applicable)

**Grading bonus:**
- Accepted PR with minor improvement: +2 points on final grade
- Accepted PR with substantial improvement: +5 points on final grade
- Multiple accepted PRs: Additional points per PR!

**Tips for a successful PR:**
- Check existing issues for ideas
- Run any code examples to ensure they work
- Follow the existing format and style
- Write clear commit messages
- Be responsive to feedback

### Exercise 4: Resolve a Merge Conflict

Simulate and resolve a conflict:

```bash
# 1. Create a repo with conflict potential
mkdir conflict-practice && cd conflict-practice
git init
echo "Line 1
Line 2
Line 3" > file.txt
git add file.txt
git commit -m "Initial file"

# 2. Create two branches
git checkout -b feature-a
echo "Line 1 - Modified by A
Line 2
Line 3" > file.txt
git commit -am "Modify line 1 in feature-a"

git checkout main
git checkout -b feature-b
echo "Line 1 - Modified by B
Line 2
Line 3" > file.txt
git commit -am "Modify line 1 in feature-b"

# 3. Merge first branch (no conflict)
git checkout main
git merge feature-a

# 4. Merge second branch (conflict!)
git merge feature-b

# 5. Resolve the conflict and commit
```

## Common Git Scenarios

### "I committed to the wrong branch!"

```bash
# If you haven't pushed yet:
git checkout correct-branch
git cherry-pick main       # Copy the commit
git checkout main
git reset --hard HEAD~1    # Remove from wrong branch
```

### "I need to undo a pushed commit!"

```bash
# Safe way - create a new commit that undoes changes
git revert abc123          # Creates new commit undoing abc123
git push
```

### "I want to clean up my commit history before PR"

```bash
# Squash multiple commits into one
git rebase -i HEAD~3       # Interactive rebase last 3 commits
# Change 'pick' to 'squash' for commits to combine
```

### "I accidentally committed a huge file!"

```bash
# Remove file from history (before pushing!)
git rm --cached large_file.zip
git commit --amend
```

## Git Workflow Strategies

### Feature Branch Workflow (Recommended for this class)

```bash
main
  └── feature-login
  └── feature-search
  └── bugfix-crash

# Each feature gets its own branch
# Merge back to main when complete
```

### Git Flow (Complex projects)

```bash
main (production)
  └── develop (integration)
       └── feature branches
       └── release branches
       └── hotfix branches
```

## Troubleshooting

### Common Issues and Solutions

**"Permission denied (publickey)"**
- SSH key not set up properly
- Solution: Follow SSH setup section above

**"Updates were rejected because the remote contains work"**
- Remote has changes you don't have
- Solution: `git pull --rebase` then `git push`

**"Please commit your changes or stash them"**
- You have uncommitted changes
- Solution: Either commit, stash, or discard changes

**"Detached HEAD state"**
- You're not on a branch
- Solution: `git checkout main` or create new branch

## Quick Reference

### Daily Commands Cheat Sheet

```bash
# Morning routine
git pull                   # Get latest changes

# While coding
git status                 # What changed?
git diff                   # See changes
git add .                  # Stage everything
git commit -m "message"    # Save snapshot
git push                   # Share with team

# Branching
git checkout -b feature    # New branch
git checkout main          # Switch back
git merge feature          # Combine branches

# Fixing mistakes
git stash                  # Temporary save
git reset --hard HEAD      # Discard all changes
git commit --amend         # Fix last commit
```

## Resources

📚 **Essential Reading:**
- [Pro Git Book (free)](https://git-scm.com/book) - The definitive guide
- [GitHub's Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Fixing common mistakes

🎮 **Interactive Learning:**
- [Learn Git Branching](https://learngitbranching.js.org/) - Visual and interactive
- [GitHub Skills](https://skills.github.com/) - Official GitHub courses
- [Git Immersion](https://gitimmersion.com/) - Hands-on tutorial

🛠 **Tools:**
- [GitHub CLI](https://cli.github.com/) - GitHub from terminal
- [Tig](https://jonas.github.io/tig/) - Text-mode interface for Git
- [Git Graph Extension](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) - VS Code extension

📝 **Best Practices:**
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

---

**Remember:** Git is a skill you'll use every single day as a developer. The more you practice, the more natural it becomes. Don't be afraid to experiment - you can almost always undo mistakes in Git!

**Next Steps:** Start using Git for ALL your projects, even personal ones. The practice will make you fluent by the time you're job hunting.