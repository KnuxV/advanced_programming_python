# Git Story Hunt: The Missing Chapter

## Your Mission
You're helping a novelist who has a problem. She's been using Git to keep track of her story changes - each commit is like saving a new version of her work. Last week, they were making Chapter 3 of her mystery novel, it seemed good, but now something's wrong. The evidence doesn't match the suspect anymore, and she can't figure out what changed!

Your job: Use Git to investigate the story's history and find out what went wrong.

## Getting Started

First, copy this instruction file (README) to an answer file so you can fill in your answers:
```bash
# INPUT_FILE is the file you want to copy
# OUPUT_FILE is the name you want to give to the copy
cp INPUT_FILE OUTPUT_FILE
```


You'll work with a Git repository containing `chapter3.txt`. The story has a plot hole that breaks the mystery's logic. Your task is to use Git commands to track down when and how this happened.

## Task 1: Read the Current Story
First, understand what's wrong:

```bash
cat chapter3.txt
```

Read through the entire story. Pay attention to:
- What evidence was found at the crime scene?
- Who are the suspects?
- Do the clues actually point to the right person?

**Question**: What doesn't make sense about the evidence and the suspects?

## Task 2: Investigate the Story's History

Use Git to see how this story evolved. Remember, each commit represents a saved version of the story:

```bash
# See all the commits (story versions)
git log --oneline

# See more detailed commit history
git log
```

You'll see output like:
```
a1b2c3d (HEAD -> main) Add forensics results to build tension
e4f5g6h Fix character description for consistency
i7j8k9l Major plot twist - introduce Professor Williams
...
```

**Git concepts to understand:**
- **HEAD**: Points to your current version (like "you are here")
- **Commit hash** (like `a1b2c3d`): Unique ID for each version
- **HEAD~1**: The previous version, **HEAD~2**: two versions back, etc.

**Questions**: 
- How many times was this story edited?
- What do the commit messages tell you about what changed?

## Task 3: Travel Back in Time First

Let's start by finding and visiting the very first commit:

```bash
# Get the full commit history
git log --oneline

# Find the first commit (at the bottom of the list)
# Copy its commit hash (like a1b2c3d)
```

Now checkout that first commit using its hash:
```bash
# Use the actual commit hash you found
git checkout commit_hash

# Read that version
cat chapter3.txt
```

**Git tip**: You only need the first few characters of the commit hash! Git can figure out which commit you mean. You can even use Tab completion:
```bash
# If the hash is a1b2c3d4e5f, you can just type:
git checkout a1b2c
# Or even:
git checkout a1b<TAB>  # Tab will complete it for you!
```

Try different versions, you can keep using the commit hash or use HEAD~n where n is the number of commit you want to rewind:
```bash
# Try different commits using their hashes or HEAD notation
git checkout HEAD~2  # 2 commits back from wherever HEAD is
git checkout HEAD~1  # 1 commit back

# Return to the latest version
git checkout HEAD
cat chapter3.txt
```

**Questions**:
- Which version of the story makes the most sense?
- At what point did the story logic start to break?
- Can you spot where the evidence stopped matching the suspect?

## Task 4: See Exactly What Changed

Now that you have a sense of which commits might be problematic, use `git show` to see the exact changes. You can focus on just the story file:  

git show COMMIT always shows: "What changed in COMMIT compared to its parent"

```bash
# See what changed in the most recent commit to chapter3.txt
git show HEAD chapter3.txt

# See changes in the second-to-last commit  
git show HEAD~1 chapter3.txt
git show HEAD~2 chapter3.txt
etc...

# See changes in a specific commit (use the actual hash)
git show a1b2c3d chapter3.txt
```

**How `git show` works**: It compares the file from the commit you specify with the previous version of that file, showing you:
- What lines were removed (marked with -)
- What lines were added (marked with +)

**Questions**:
- Which commit seems to have broken the story logic?
- What specific text was changed?
- What should that text say instead to fix the plot hole?

## Task 5: Understanding the Timeline

Put the pieces together:

```bash
# See all changes to just the story file
git log -p chapter3.txt
# You can press the down arrow or ENTER to scroll down
```

This shows the complete evolution of your story file.

**Questions**:
- Can you now identify the exact commit that broke the logic?
- What was the story like before and after that commit?

## Task 6: Fix the Plot Hole

Now let's actually solve the mystery! To fix the plot hole, we need to find where Marcus was first described with red clothing and restore that description.

### Step 1: Search for the evidence
Use `git grep` to search through old versions:

```bash
# Search for "red" in different commits
git grep "red" HEAD~1
git grep "red" HEAD~2

# Use regex to find exact word matches (not "red" inside other words)
git grep "\bred\b" HEAD~2
```

The `\b` in regex means "word boundary" - so `\bred\b` finds "red" as a complete word, not "answered" or "Reddit".

### Step 2: Find the right description
Once you find a commit where Marcus is described with red clothing, checkout that version:

```bash
# Go to the commit with the correct description
git checkout HEAD~2  # or whatever commit has the right version
cat chapter3.txt
```

### Step 3: Fix the current version
Go back to the latest version and fix it:

```bash
# Return to the latest version
git checkout main

# Edit chapter3.txt to change Marcus's clothing back to red
# (Use any text editor to make the change)

# Create a new commit with your fix
git add chapter3.txt
git commit -m "Fix Marcus clothing description - restore red sweater for plot consistency"
```

## Git Commands Summary

```bash
git log # See commit history with details
git log --oneline # Shorter commit history
git log -p filename # See actual changes to a file over time

git show commit filename # See what changed to a specific file in a commit

git checkout commit_hash # Go back to an old version (use hash or HEAD~N)
git checkout main  # Return to latest version

git grep "pattern" commit_hash  # Search for text in old versions
git grep "pattern" file_name  # Search for text in old versions

git add  
git commit # Save your changes as a new version
```