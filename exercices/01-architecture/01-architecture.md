---
layout: page
title: "Exercise 1: Project Architecture"
class_number: 1
date: 2025-08-01
due_date: "Week 2"
difficulty: "Beginner"
estimated_time: "45 minutes"
topics: ["linux", "shell", "project-structure"]
---

# Exercise 1: Project Architecture


## Task Overview
Create the structure of folder and subfolders to match the target structure below and place the files in their rightful spot. 

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
   sudo apt install tree # This will install the command tree if it is not already available
   # Navigate to the root of the economics_project folder
   tree 
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
   # you can use the already installed text-editor called `nano`
   # But you will find micro to be just like windows, CTRL+S = save, CTRL+Q = Quit
   sudo apt install micro 
   micro my_file
   ```
   2. Add basic project information:
      - Project title and description
   3. Save and exit nano:
      - `Ctrl+S` to save (write out)
      - `Ctrl+Q` to exit
   4. Verify your README was created:
   ```bash
   cat README.md
   ```
---