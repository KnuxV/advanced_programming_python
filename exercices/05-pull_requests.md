---
layout: page
title: "Department SQL Class Exercise"
class_number: 3
date: 2025-08-01
difficulty: "Intermediate"
estimated_time: "90 minutes"
topics: ["sql", "python", "data-analysis"]
---

# Git Pull Request Exercise: Contribute to Class Resources

## Your Mission
Make a meaningful contribution to our class resources and earn bonus points (0.5 to 1 pt) for your final grade!

It does not have to be on the first day, you can do it **anytime**.

## Choose Your Target Repository


**Option A: Website (GitHub)**
- Repository: https://github.com/KnuxV/advanced_programming_python
- Good for: Adding resources, fixing typos, improving documentation

**Option B: Git Exercises (GitLab Unistra)**  
- Repository: https://gitlab.unistra.fr/cours_git
- Good for: Adding exercises, corrections, translations, clarifications
- Login with your regular Unistra credentials

## What Contributions Are Worth Bonus Points?

**High value (1 pt):**
- Add a new exercise or tutorial
- Translate existing content to another language
- Add substantial documentation or resources
- Create comprehensive solution guides

**Basic value (0.5 pt):**
- Fix typos and grammar
- Add small improvements or corrections
- Minor formatting fixes
- Fix bugs or issues
- Add useful clarifications to existing exercises
- Improve existing documentation structure
- Provide alternative exercise solutions

## Step-by-Step Instructions

### 1. Fork the Repository
- Go to your chosen repository URL
- Click **"Fork"** button
- You now have your own copy in your account

### 2. Clone Your Fork to your local machine
```bash
# Replace YOUR_USERNAME and choose github.com OR gitlab.unistra.fr
git clone https://github.com/YOUR_USERNAME/advanced_programming_python
# OR
git clone https://gitlab.unistra.fr/YOUR_USERNAME/cours_git

cd repository-name
```

### 3. Create a Feature Branch
```bash
# Choose a descriptive name
git switch -c fix-typos-chapter3
# OR
git switch -c add-french-translation
# OR  
git switch -c improve-merge-exercise
```

**Important:** Never work directly on your main branch!

### 4. Make Your Changes
- Edit files, add content, fix issues
- Test that everything works
- Make sure your changes are useful!

### 5. Commit Your Work
```bash
git add .
git commit -m "Fix typos in Git merge exercise

- Correct spelling errors in instructions
- Improve clarity of conflict resolution steps"
```

### 6. Push Your Feature Branch
```bash
# Only push when you're satisfied with your changes
git push origin your-branch-name
```

### 7. Create Pull Request
- After pushing, both GitHub/GitLab will show a helpful banner
- Click **"Create Pull Request"** or **"Create Merge Request"**
- The PR goes: `your-username/feature-branch` → `original-repo/main`
- Write a clear description of what you changed and why

### 8. Wait for Review
- Your instructor will review and provide feedback
- Make additional changes if requested
- Celebrate when it gets merged! 🎉

## Contribution Ideas

**For the Website:**
- Add useful Python resources, links or explanations about the class
- Fix documentation errors
- Improve exercise instructions, suggest variants
- Add examples or clarifications

**For Shell, Git and Python Exercises:**
- Add translations (create branch like `french-translation` with a mention of the branch in the instructions)
- Clarify confusing instructions
- Add new practice exercises
- Fix bugs in existing exercises
- Provide solution guides
- Add "common mistakes" sections
- Create troubleshooting guides

## Example Pull Request Description
```markdown
## What I Changed
Fixed multiple typos and unclear instructions in the merge conflict exercise.

## Why This Helps
- Students were confused by step 4
- Several spelling errors made instructions hard to follow
- Added clearer examples for beginners

## Files Changed
- exercises/merge-conflict.md
- README.md (minor formatting)


```

## Important: PR Direction

You are creating a PR **from your feature branch to the original repository's main branch**:
- ✅ `your-fork/feature-branch` → `original-repo/main`
- ❌ NOT to your own main branch

You don't need to merge your feature branch into your main branch first!

## Quick Commands Reference
```bash
# Basic workflow
git clone your-fork-url
cd repository-name
git switch -c your-branch-name
# ... make changes ...
git add .
git commit -m "Clear description of changes"
git push origin your-branch-name
# Then create PR on the website
```

## Tips for Success
- **Be specific**: Target one clear improvement, make several specific pull requests instead of a big complicated one. 
- **Test everything**: Make sure your changes work
- **Explain clearly**: Write good commit messages and PR descriptions
- **Start small**: Better to make a small, perfect contribution than a large, messy one A pull request must follow a thematic. If you are fixing typos, it's okay to target many different files because the theme is to fix typo. But don't fix typo and add a translation in the same pull request.
- **Focus on helping future students**: Think about what would be most useful

## Common Mistakes to Avoid
- Working directly on main branch instead of a feature branch
- Pushing untested changes
- Making PRs that are too large or unfocused
- Not explaining what you changed or why
