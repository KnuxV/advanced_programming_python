
# Git Merge Conflict Exercise: Scrabble Score Calculator

Exercice with Branches and merge.
##  The exercice is available on my GITLAB: https://gitlab.unistra.fr/cours_git/exercise_scrabble

## What You'll Learn

- How to create and switch between Git branches
- How to merge branches
- What merge conflicts are and how to resolve them
- Real-world collaborative development workflow

## Exercise Overview

You have a basic Scrabble score calculator, and two developers have independently added different features:

- **Feature 1**: Letter multipliers (double/triple letter scores)
- **Feature 2**: Word multipliers (double/triple word scores)

Your job is to merge both features together, which will create a merge conflict that you need to resolve.

## Git Concepts You Need to Know

### What is a Branch?

A **branch** is like a separate timeline for your code. It allows you to work on features independently without affecting the main codebase.

- `main` - The primary branch with stable code
- `letter-multiplier` - A branch for developing letter bonus functionality  
- `word-multiplier` - A branch for developing word bonus functionality

Think of it like this:
```
main:           A---B---C -------G
                     \         /
feature-branch:       D---E---F
```

### Basic Branch Commands

**Create a new branch:**
```bash
git branch <branch-name>
```

**Switch to a branch:**
```bash
git switch <branch-name>
```

**Create and switch in one command:**
```bash
git switch -c <branch-name>
```

**See all branches:**
```bash
git branch
```

**See current branch:**
```bash
git branch --show-current
```

### Merging Branches

**Merging** combines the changes from one branch into another. If you want to merge the changes made on a feature branch to your main branch, you must be first switch to the main branch.

```bash
git switch main                      # Switch to target branch
git merge letter-multi               # Merge the feature branch
```

### Important: Saving Your Work Before Switching

**Always commit your changes before switching branches!**

```bash
git add .                           # Stage your changes
git commit -m "Your commit message" # Save your changes
git switch other-branch             # Now it's safe to switch
```

**What happens if you don't commit before switching?**

Git will either:
1. **Block the switch** if you have conflicting changes:
   ```
   error: Your local changes would be overwritten by checkout.
   Please commit your changes or stash them before you switch.
   ```

2. **Take your changes with you** if there are no conflicts - this can be confusing because your uncommitted changes appear on the new branch!

**Best practice:** Always commit your work before switching branches. This keeps each branch's history clean and prevents confusion.

When you merge, Git tries to automatically combine the changes. Sometimes it succeeds, sometimes it doesn't...

### What is a Merge Conflict?

A **merge conflict** happens when Git can't automatically figure out how to combine changes. This occurs when:

- The same lines of code were modified differently in both branches
- One branch modified a line that another branch deleted
- The same function was changed in incompatible ways

When this happens, Git stops and asks YOU to decide how to resolve the conflict.

## Exercise Instructions

### Step 1: Set Up the Repository

1. Clone or download [this repository](https://gitlab.unistra.fr/cours_git/exercise_scrabble)
2. Make sure you're on the `main` branch:
   ```bash
   git switch main
   ```
3. Look at the base `scrabble_score.py` file to understand the basic functionality

### Step 2: Explore the Feature Branches

**Check the number and names of other branches (features)**
```bash
git branch
```

**Check out the first feature branch:**
```bash
git switch branch_name
```
- Run the script and see what's different
- Look at how the `calculate_score()` function changed
- Note what new functionality was added

**Check out the second feature branch:**
```bash
git switch branch_name
```
- Run this version too
- Compare the `calculate_score()` function to the letter-multi version
- See what different functionality was added

**Return to main:**
```bash
git switch main
```

### Step 3: Attempt the Merge

**First merge (this should work smoothly):**
```bash
git merge one_of_the_two_branch_name
```
- This should succeed without conflicts
- Test the script to make sure it works

**Second merge (this will create a conflict!):**
```bash
git merge the_second_branch_name
```
- Git will stop and tell you there's a conflict
- Don't panic! This is expected.

### Step 4: Understanding the Conflict

When the conflict occurs, Git will show you something like:
```
Auto-merging scrabble_score.py
CONFLICT (content): Merge conflict in scrabble_score.py
Automatic merge failed; fix conflicts and then commit the result.
```

**Check the conflict status:**
```bash
git status
```

**Open the conflicted file** (`scrabble_score.py`) in your text editor. You'll see conflict markers:

```python
<<<<<<< HEAD
# Code from the current branch (main + letter-multi)
=======
# Code from the branch you're trying to merge (word-multiplier)
>>>>>>> word-multiplier
```

### Step 5: Resolve the Conflict

Your job is to:

1. **Understand both versions** - What does each version do?
2. **Combine the functionality** - Both features should work together
3. **Remove the conflict markers** - Delete the `<<<<<<<`, `=======`, and `>>>>>>>` lines
4. **Create a working solution** - Think about how to merge the function parameters and logic

**Hint:** Consider how you might need to modify the function signature to accept both types of parameters, and how the logic should handle both types of bonuses.

### Step 6: Complete the Merge

After resolving the conflicts:

1. **Test your solution** - Make sure both types of bonuses work
2. **Add the resolved file:**
   ```bash
   git add scrabble_score.py
   ```
3. **Complete the merge:**
   ```bash
   git commit -m "Resolve merge conflict: combine letter and word multipliers"
   ```

### Step 7: Verify Your Solution

Your final solution should be able to handle:
- Basic scoring (no bonuses)
- Letter multipliers only
- Word multipliers only  
- Both letter AND word multipliers together

## Tips for Success

- **Read the code carefully** - Understand what each version does before merging
- **Think about the domain** - How do Scrabble bonuses actually work?
- **Test as you go** - Run the script after each step to make sure it works
- **Don't just copy-paste** - Think about how to logically combine the features

## Common Mistakes to Avoid

- Don't just pick one version and ignore the other
- Don't forget to remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
- Don't merge without testing - make sure your solution actually works
- Don't panic when you see a conflict - it's a normal part of development!

## What to Do When You're Done

1. **Test your merged solution thoroughly**
2. **Make sure all Git conflicts are resolved** (`git status` should be clean)
3. **Your `main` branch should now have both features working together**

## Getting Help

If you get stuck:
- Use `git status` to see what's happening
- Look at the conflict markers carefully
- Think about what each piece of code is trying to do
- Remember: the goal is to make both features work together

Good luck! Merge conflicts might seem scary at first, but they're a normal part of collaborative development. Once you understand them, you'll be much more confident working on team projects.