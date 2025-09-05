---
layout: page
title: Shell Commands
class_number: 1
---
# Shell Commands for Data Analysis

## Creating Sample Data

We'll create a simple CSV file to work with. Copy this data to your clipboard:

```
Name,City,Age
Alice,Paris,25
Bob,Lyon,30
Claire,Nice,22
```

Now create the file using `echo` and redirect (`>`). **Make sure you're in a folder where you want to save the file:**

```bash
# Check where you are
pwd

# Create the file (paste the data with Ctrl+Shift+V)
echo "Name,City,Age
Alice,Paris,25
Bob,Lyon,30
Claire,Nice,22" > filename.csv
```

The `>` symbol **redirects** the output of `echo` into a new file called `filename.csv` instead of showing it on screen.

### Adding More Data with Append (`>>`)

To add a new row without overwriting the existing file, use `>>`:

```bash
# Add another person to our data
echo "David,Marseille,28" >> filename.csv

# Check that it was added
cat filename.csv
```

Notice: `>` creates/overwrites a file, `>>` adds to the end of an existing file.

## Basic File Commands

### `head` - Show First Lines
```bash
head filename.csv           # First 10 lines (default)
head -3 filename.csv        # First 3 lines
head -1 filename.csv        # Just the first line, that is the header
```

### `tail` - Show Last Lines  
```bash
tail filename.csv           # Last 10 lines (default)
tail -2 filename.csv        # Last 2 lines
tail -n +2 filename.csv     # From line 2 onwards (skip header!)
# Also Think and try
tail -n filename.csv # what will happen ?
tail -n+1 filename.csv # what will happen?
```

### `sort` - Sort Lines
```bash
sort data.csv               # Basic alphabetical sort (by whole line)
```

**Key options:**
- `-r` = reverse the sort order (Z to A instead of A to Z)
- `-t','` = tell sort that columns are separated by commas
- `-k2` = sort by the 2nd column
- `-n` = sort numbers properly (10 comes after 2, not before)

**Examples:**
```bash
sort -r data.csv                    # Reverse alphabetical
sort -t',' -k2 data.csv            # Sort by City column
sort -t',' -k3,3n data.csv         # Sort by Age column (numerically)
sort -t',' -k2 -r data.csv         # Sort by City, reverse order
```

**You can combine options:**
```bash
sort -t',' -k3,3nr data.csv        # Sort by Age, numerically, reverse (oldest first)
```

## The `cut` Command

`cut` extracts specific columns from text files using delimiters.

### How Column Numbers Work
**Important:** `cut` doesn't read column names! It just counts delimiters:
- Column 1: everything before the first comma
- Column 2: between first and second comma  
- Column 3: between second and third comma

```bash
# Basic syntax
cut -d',' -f1 filename.csv     # First column (Name)
cut -d',' -f2 filename.csv     # Second column (City)  
cut -d',' -f1,3 filename.csv   # Columns 1 and 3 (Name,Age)
cut -d',' -f2- filename.csv    # From column 2 onwards
cut -d',' -f-2  filename.csv   # From the first column to the second.
```
## Pipes (|) - Chaining Commands

Pipes send output from one command as input to the next:

```bash
command1 | command2
```

### Skip the Header
```bash
# Get just the data (no header)
cut -d',' -f1 filename.csv | tail -n +2
>results:
    Alice
    Bob
    Claire
    David

# Get names without header, then sort in reverse
cut -d',' -f1 filename.csv | tail -n +2 | sort -r
>results:
    David
    Claire
    Bob
    Alice

```




### Example
```bash
# Get cities, skip header, sort them, show unique ones
cut -d',' -f2 filename.csv | tail -n +2 | sort | uniq
```

This chain:
1. Extracts the City column
2. Removes the header line  
3. Sorts the cities alphabetically
4. Shows only unique cities

## Redirecting Output (>)

Save command results to a file instead of displaying on screen:

```bash
# Save all names to a file
cut -d',' -f1 filename.csv > names.txt

# Save sorted cities 
cut -d',' -f2 filename.csv | tail -n +2 | sort > cities.txt

# Append to existing file (use >>)
cut -d',' -f1,2 filename.csv >> backup.csv
```

### Quick Example Workflow
```bash
# 1. Look at the data
head filename.csv

# 2. Extract just names and ages, save to new file  
cut -d',' -f1,3 filename.csv > names_ages.csv

# 3. Get sorted list of cities
cut -d',' -f2 filename.csv | tail -n +2 | sort > city_list.txt
```

# Shell Commands Exercise

Use the `grades.csv` file for these exercises. Remember to check your current directory with `pwd` first!

## Warm-up Questions

**1. Basic exploration**
- How many students are in the class? (answer: 49)
- Show just the first 3 students with all their information

**2. Names and structure**
- Extract and save all student first names to a file called `first_names.txt`
- Get both first and last names, skip the header, and sort them alphabetically

## Subject Analysis

**3. Math performance**
- Extract all Algèbre grades (columns 3, 4, 5) and save to `algebra_grades.csv`
- Find the 5 highest first Algèbre grades (Algèbre1 column)

**4. Literature focus**
- Get all Dissertation grades (columns 9, 10) for analysis
- Show students sorted by their first Commentaire grade (from lowest to highest)

## Advanced Combinations

**5. Student comparison**
- Find all students whose first name starts with 'A' (Hint: use `grep` after extracting names)
- Create a file with just names and first grades of each subject (columns 1, 2, 3, 6, 9, 11)

**6. Data organization**
- Sort all students by last name and save the result to `students_by_lastname.csv`
- Extract unique first names and count how many there are

## Challenge Questions

**7. Pattern finding**
- Who has the highest single grade in Algèbre1? Show their full name and grade
- Create separate files for math specialists vs literature specialists:
  - `math_students.csv`: Students with Algèbre1 ≥ 16
  - `lit_students.csv`: Students with Dissertation1 ≥ 16

**Sample command to get you started:**
```bash
# Question 1 example:
head -1 students_grades.csv  # Check the header
tail -n +2 students_grades.csv | wc -l  # Count students
```

**Bonus:** Try to chain multiple commands with pipes to answer these in one line each!