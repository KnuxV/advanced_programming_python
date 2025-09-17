# Git Terminal Discovery Session - To-Do List

## Pre-Session Setup (5 minutes)
- [ ] Open terminal/command prompt
- [ ] Navigate to desktop or projects folder
- [ ] Verify Git is installed: `git --version`
- [ ] Have GitHub account ready (students should already have one)

## Session Opening (10 minutes)
- [ ] `git status`
- [ ] Show the flow: Working Directory → Staging → Local Repo → Remote

## Live Demo Setup (15 minutes)
- [ ] Create project folder
- [ ] Initialize: `git init` 
- [ ] ls -la` (show the hidden `.git` folder)
- [ ] `git status` (clean working tree)

## First File Experience (20 minutes)
- [ ] `echo "# Stuff > README.md`
- [ ] `git status` - discuss "untracked files"
- [ ] `git add README.md`
- [ ] `git status` again - discuss green vs red
- [ ] `git commit -m "Initial commit: Add project README"`
- [ ] `git log` - show the commit hash, author, date

## Build Momentum (25 minutes)
- [ ] **Made modifications, add new files** 
- [ ] **Check changes**: `git diff` (show before staging)
- [ ] **Stage**: `git add calculator.py`
- [ ] **Check staged**: `git diff --staged`
- [ ] **Commit**: `git commit -m "Add Comments"`
- [ ] **History**: `git log --oneline` (show the progression)

## GitHub Connection (15 minutes)
- [ ] **Create repo on GitHub** (walk through web interface)
- [ ] **Set-up SSH or 
- [ ] **Connect**: `git remote add origin [SSH-URL]`
- [ ] **Verify**: `git remote -v`
- [ ] **Push**: `git push -u origin main`
- [ ] **Success check**: Refresh GitHub page together

