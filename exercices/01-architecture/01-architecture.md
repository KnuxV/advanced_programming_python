---
layout: page
title: "Exercise 1: Project Architecture"
date: 2025-08-01
due_date: "Week 2"
difficulty: "Beginner"
estimated_time: "45 minutes"
topics: ["linux", "shell", "project-structure"]
---

# Exercise 1: Project Architecture

## Learning Objectives
By the end of this exercise, you will be able to:
- Set up a proper project folder structure
- Navigate directories using shell commands
- Create and organize files for data analysis projects
- Use basic shell commands for file management

## Prerequisites
- Completed [Linux Shell Introduction](../lessons/01-shell-intro.md)
- Access to a terminal (WSL, Mac Terminal, or Linux)

---

## Task Overview
You have a messy collection of files that need to be organized into a proper project structure. Transform the chaos into a clean, professional economics project layout using shell commands to move, copy, delete, rename, and create new files and folders.

## Starting Files
You should find these files in your exercise directory:
- `1.txt`, `2.txt`, `3.txt`, `4.txt`, `5.txt` (raw data files)
- `neg_fake_negs.parquet` (processed dataset)
- `01-bubble_all_pubs_intersection.png` (visualization)
- `02_bubble_review_pubs_intersection.png` (another visualization)

## Target Structure
Transform your messy directory into this organized structure:
```
economics_project/
├── data/
│   ├── raw/
│   │   ├── 1.txt
│   │   ├── 2.txt
│   │   ├── 3.txt
│   │   ├── 4.txt
│   │   └── 5.txt
│   └── processed/
│       └── neg_fake_negs.parquet
├── scripts/
├── results/
│   ├── figures/
│   │   ├── 01-bubble_all_pubs_intersection.png
│   │   └── 02_bubble_review_pubs_intersection.png
│   └── tables/
├── docs/
└── README.md
```

## Instructions

### Part 1: Create the Project Structure

1. **Create the main project directory and navigate into it (mkdir and cd)**

2. **Create all necessary subdirectories (mkdir and cd)**


3. **Verify your structure**
   ```bash
   sudo apt install tree # if not install already
   # Navigate to the root of the economics_project folder
   tree  # or ls -R if tree isn't available
   ```

### Part 2: Organize the Files

4. **Move raw data files**
   1. We can use the command `mv`
   2. Remember that we access the parent of a folder with `..`
   3. For ex., `cd ..` moves to the parent of where I am. But you can also use `..` with `mv`
   4. We can visualize the text data with the command `cat` for ex. `cat 1.txt`


5. **Move processed data** (neg_fake_negs.parquet)


6. **Move visualization files** (bubble.png)
7. **Visualize pictures**
   - You can open pictures with the command `eog picture.png`

8. **Create a README.md file (touch)**

9. **Edit the README.md file**
   1. For editing we can use the command nano
   ```bash
   nano my_file
   ```
   2. Add basic project information:
      - Project title and description
   3. Save and exit nano:
      - `Ctrl+O` to save (write out)
      - `Ctrl+X` to exit
   4. Verify your README was created:
   ```bash
   cat README.md
   ```
---