# Exercise 1: Project Architecture - Complete Solution

## Quick Reference Commands

If you want the complete solution without explanations, here are all the commands in order:

```bash
# Create project structure
mkdir economics_project && cd economics_project
mkdir -p data/{raw,processed} scripts results/{figures,tables} docs

# Move files (assuming you're in economics_project and files are in parent directory)
mv ../1.txt ../2.txt ../3.txt ../4.txt ../5.txt data/raw/
mv ../neg_fake_negs.parquet data/processed/
mv ../01-bubble_all_pubs_intersection.png ../02_bubble_review_pubs_intersection.png results/figures/

# Create README
touch README.md
```

## Detailed Step-by-Step Solution

### Prerequisites
Make sure you're in the directory containing these starting files:
- `1.txt`, `2.txt`, `3.txt`, `4.txt`, `5.txt`
- `neg_fake_negs.parquet`
- `01-bubble_all_pubs_intersection.png`
- `02_bubble_review_pubs_intersection.png`

### Part 1: Create the Project Structure

**Step 1: Create main project directory**
```bash
mkdir economics_project
cd economics_project
```

**Step 2: Create all subdirectories efficiently**
```bash
# Create all directories at once using brace expansion
mkdir -p data/{raw,processed} scripts results/{figures,tables} docs
```

Alternative method (step by step):
```bash
mkdir data scripts results docs
mkdir data/raw data/processed
mkdir results/figures results/tables
```

**Step 3: Verify structure**
```bash
# Install tree if needed
sudo apt install tree

# View the structure
tree
```

Expected output:
```
economics_project/
├── data/
│   ├── processed/
│   └── raw/
├── docs/
├── results/
│   ├── figures/
│   └── tables/
└── scripts/

7 directories, 0 files
```

### Part 2: Organize the Files

**Step 4: Move raw data files**
```bash
# Move all .txt files at once
mv ../1.txt ../2.txt ../3.txt ../4.txt ../5.txt data/raw/

# Alternative: using wildcards (if only .txt files exist)
# mv ../*.txt data/raw/
```

**Step 5: Move processed data**
```bash
mv ../neg_fake_negs.parquet data/processed/
```

**Step 6: Move visualization files**
```bash
mv ../01-bubble_all_pubs_intersection.png results/figures/
mv ../02_bubble_review_pubs_intersection.png results/figures/
```

**Step 7: Create README.md**
```bash
touch README.md
```

**Step 8: Edit README.md**
```bash
# Install micro (more user-friendly editor)
sudo apt install micro

# Edit the file
micro README.md
```

**README.md content to add:**
```markdown
# Economics Research Project

## Description
This project analyzes economic data using various datasets and generates visualizations to understand publication patterns and intersections.

## Project Structure
```
economics_project/
├── data/
│   ├── raw/           # Original, unprocessed data files (1.txt - 5.txt)
│   └── processed/     # Clean, processed datasets (neg_fake_negs.parquet)
├── scripts/           # Analysis and processing scripts
├── results/
│   ├── figures/       # Generated visualizations (bubble charts)
│   └── tables/        # Generated tables and summaries
├── docs/              # Documentation and reports
└── README.md          # Project documentation
```

## Data Description
- **Raw data files (1.txt - 5.txt)**: Original economic indicator data
- **Processed data (neg_fake_negs.parquet)**: Cleaned dataset ready for analysis
- **Visualizations**: 
  - 01-bubble_all_pubs_intersection.png: All publications intersection analysis
  - 02_bubble_review_pubs_intersection.png: Review publications intersection analysis

## Getting Started
1. Place your analysis scripts in the `scripts/` directory
2. Run analyses from the project root directory
3. Output files will be saved in `results/figures/` or `results/tables/`
4. Document your findings in the `docs/` directory

## Requirements
- Python 3.x
- pandas (for data processing)
- matplotlib/seaborn (for visualizations)
```

Save and exit:
- In micro: `Ctrl+S` (save), then `Ctrl+Q` (quit)
- In nano: `Ctrl+O` (save), then `Ctrl+X` (exit)

### Part 3: Final Verification

**Step 9: Verify everything is in place**
```bash
# Check the complete structure
tree

# Verify files are in correct locations
echo "Raw data files:"
ls data/raw/

echo "Processed data:"
ls data/processed/

echo "Figures:"
ls results/figures/

echo "README content:"
cat README.md
```

**Step 10: Test file access**
```bash
# View a text file
cat data/raw/1.txt

# View images (if in GUI environment)
eog results/figures/01-bubble_all_pubs_intersection.png
```

## Final Expected Structure

After completing all steps, your directory should look exactly like this:

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

## Common Troubleshooting

### Problem: "No such file or directory"
**Solution:** Check your current location
```bash
pwd                    # Show current directory
ls ../                 # List files in parent directory
```

### Problem: Tree command not found
**Solution:** Use alternative visualization
```bash
find . -type d | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
```

### Problem: Permission denied
**Solution:** Check file permissions
```bash
ls -la ../             # Check permissions of source files
```

### Problem: Files already exist
**Solution:** Use force move (be careful!)
```bash
mv ../1.txt data/raw/  # This will overwrite existing files
```

## Alternative Approaches

**Using absolute paths (if you know the full path):**
```bash
# Instead of ../
mv /home/username/path/to/files/1.txt data/raw/
```

**Creating directories and moving in one line:**
```bash
mkdir -p data/raw && mv ../1.txt ../2.txt ../3.txt ../4.txt ../5.txt data/raw/
```

**Using find to locate files:**
```bash
# If you're not sure where files are
find . -name "1.txt" 2>/dev/null
```

## Validation Commands

Run these commands to ensure everything is correct:

```bash
# Should show 5 .txt files
ls data/raw/ | wc -l

# Should show 1 .parquet file
ls data/processed/ | wc -l

# Should show 2 .png files
ls results/figures/ | wc -l

# Should show directory exists
ls -ld scripts docs results/tables
```

If all commands return expected results, your exercise is complete!
