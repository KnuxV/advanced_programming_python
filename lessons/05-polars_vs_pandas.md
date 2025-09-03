# Polars vs Pandas: Modern DataFrames in Python

## Quick Pandas Refresher (5 min)

### What is Pandas?
- **Industry standard** for data manipulation in Python since 2008
- Built on NumPy, single-threaded by design
- You've used it, you'll probably use it again (legacy code, tutorials, Stack Overflow)

### The Good and The Messy with Pandas

```python
import pandas as pd

# Reading data - familiar territory
df = pd.read_csv('data.csv')
df = pd.read_sql('SELECT * FROM table', connection)

# The indexing maze - remember this confusion?
df['column_name']           # Returns Series
df[['column_name']]         # Returns DataFrame
df.column_name              # Works until it doesn't (spaces, reserved words)
df.loc[0, 'column_name']    # Label-based
df.iloc[0, 1]               # Position-based
df.at[0, 'column_name']     # Fast scalar access
```

### Common Pandas Patterns
```python
# Filtering and transforming
df[df['age'] > 25]
df.groupby('category').agg({'price': 'mean'})
df['new_col'] = df['col1'] * 2
```

### The Performance Problem
- **Single-core execution** - wastes your modern CPU
- In-place operations vs copies - constant memory anxiety
- Index alignment - sometimes helpful, often surprising

---

## Enter Polars: DataFrames for the Modern Era (20 min)

### Why Polars? The Elevator Pitch
- Written in **Rust** 🦀 - memory safe, blazingly fast
- **Multi-threaded by default** - uses all your CPU cores
- **Columnar memory layout** - cache-friendly operations
- **Lazy evaluation** - optimize before executing
- **No index** - one less thing to worry about
- Cleaner, more predictable API

### Performance Comparison
```python
# Pandas: Single core suffering
df.groupby('category').agg({'value': 'sum'})  # ☕ Time for coffee

# Polars: All cores working
df.group_by('category').agg(pl.col('value').sum())  # ⚡ Already done
```

**Benchmarks show 5-10x speedups on common operations, sometimes 50x+ on large datasets**

### Getting Started with Polars
```python
import polars as pl

# Reading data - familiar but better
df = pl.read_csv('data.csv')
df = pl.read_parquet('data.parquet')  # First-class Parquet support

# Database operations - built-in!
df = pl.read_database("SELECT * FROM table", connection_string)
df.write_database("new_table", connection_string)
```

### The Polars Way: Expression API

Everything is an **expression** - composable, optimizable, readable:

```python
# Select columns
df.select(
    pl.col('name'),
    pl.col('age'),
    pl.col('salary')
)

# Filter rows - notice the cleaner syntax
df.filter(pl.col('age') > 25)

# Add computed columns
df.with_columns(
    (pl.col('salary') * 1.1).alias('new_salary'),
    (pl.col('age') + 1).alias('next_year_age')
)

# Chain operations - reads like SQL!
result = (
    df
    .filter(pl.col('age') > 25)
    .with_columns(
        (pl.col('salary') * 1.1).alias('adjusted_salary')
    )
    .select(['name', 'adjusted_salary'])
)
```

### SQL-like Operations You Already Know

```python
# Group by and aggregate
df.group_by('department').agg(
    pl.col('salary').mean().alias('avg_salary'),
    pl.col('age').max().alias('max_age'),
    pl.len().alias('count')
)

# Joins - explicit and clear
df1.join(df2, on='id', how='left')

# Window functions
df.with_columns(
    pl.col('salary').rank().over('department').alias('salary_rank')
)
```

### Lazy Evaluation: Work Smarter, Not Harder

**Why lazy evaluation matters**: When you use lazy operations, Polars doesn't execute anything immediately. Instead, it builds a query plan - a recipe of all the operations you want to perform. This allows Polars to optimize the entire pipeline before execution. It can reorder operations, push filters down to reduce data early, eliminate unnecessary work, and even combine multiple operations into single passes through the data. Think of it like a SQL query optimizer - the database doesn't just execute your query line by line, it figures out the smartest way to get your result. Polars does the same thing.

```python
# Create a lazy frame
lazy_df = pl.scan_csv('huge_file.csv')  # Doesn't load yet!

# Build your query plan
result = (
    lazy_df
    .filter(pl.col('year') == 2024)
    .filter(pl.col('status') == 'active')  # Multiple filters
    .select(['category', 'amount', 'quantity'])  # Select columns
    .with_columns(
        (pl.col('amount') * pl.col('quantity')).alias('total')
    )
    .group_by('category')
    .agg(pl.col('total').sum())
)

# Polars optimizes before executing:
# - Combines both filters into one operation
# - Only reads needed columns from CSV (ignores the rest)
# - Pushes filters down to read level (reads less data)
# - Reorders operations for maximum efficiency

final_result = result.collect()  # NOW it executes the optimized plan
```

### Processing Larger-than-RAM Datasets

**Streaming mode explained**: When you add `streaming=True` to your collect(), Polars switches to a completely different execution model. Instead of loading all data at once, it processes your dataset in chunks that fit comfortably in memory. Each chunk flows through your operations pipeline, and Polars intelligently manages intermediate results. This means you can process a 100GB file on a laptop with 8GB RAM - something that would make pandas immediately crash with an out-of-memory error.

**Sink operations - the ultimate streaming**: The `sink_parquet()` and `sink_csv()` operations take streaming even further. Instead of collecting results into memory at all, they write directly to disk as data is processed. This is perfect for ETL pipelines where you're transforming massive datasets. The data flows from disk, through your transformations, and back to disk without ever fully materializing in RAM. It's like having a data pipeline rather than a data container.

```python
# Streaming mode - process massive files in chunks
huge_df = pl.scan_csv('100GB_file.csv')
result = (
    huge_df
    .filter(pl.col('amount') > 1000)
    .group_by('category')
    .agg(pl.col('amount').sum())
    .collect(streaming=True)  # Magic parameter! Processes in chunks
)

# Better: Use Parquet for big data
lazy_df = pl.scan_parquet('huge_dataset.parquet')  # Only reads needed columns
result = lazy_df.select(['col1', 'col2']).collect()  # Efficient columnar access

# Write results directly to disk - never loads full dataset in memory
(
    pl.scan_csv('massive_file.csv')
    .filter(pl.col('year') == 2024)
    .group_by(['category', 'region'])
    .agg(pl.col('sales').sum())
    .sink_parquet('aggregated_results.parquet')  # Streams directly to disk!
)

# Process partitioned datasets
for year in range(2020, 2025):
    (
        pl.scan_parquet(f'data/year={year}/*.parquet')
        .group_by('product')
        .agg(pl.col('revenue').sum())
        .sink_parquet(f'summary_{year}.parquet')
    )
```

**Why Parquet changes everything**: Parquet is a columnar file format, meaning data is stored column by column rather than row by row like CSV. This is perfect for analytics because you usually only need specific columns. When you `scan_parquet()` and select just 3 columns from a 100-column dataset, Polars only reads those 3 columns from disk - the other 97 columns are never touched. Additionally, Parquet has built-in compression and stores statistics about data chunks, allowing Polars to skip entire sections of the file if they don't match your filters. It's like having a smart index built into your file format.

**This is impossible with pandas!** Pandas needs the entire DataFrame in memory. Polars can process terabytes with just gigabytes of RAM.

### Common Operations Comparison

| Operation | Pandas | Polars |
|-----------|--------|--------|
| Select columns | `df[['col1', 'col2']]` | `df.select(['col1', 'col2'])` |
| Filter rows | `df[df['age'] > 25]` | `df.filter(pl.col('age') > 25)` |
| Add column | `df['new'] = df['old'] * 2` | `df.with_columns((pl.col('old') * 2).alias('new'))` |
| Group by | `df.groupby('x').sum()` | `df.group_by('x').sum()` |
| Sort | `df.sort_values('col')` | `df.sort('col')` |
| Join | `pd.merge(df1, df2, on='id')` | `df1.join(df2, on='id')` |

---

## Advanced Polars Features

### Nested Data Types: First-Class Citizens

Unlike pandas, Polars handles nested data structures elegantly:

```python
```python
```python
# Create a DataFrame with nested lists
df = pl.DataFrame({
    'user': ['Alice', 'Bob', 'Charlie'],
    'scores': [[85, 92, 88], [76, 81, 79], [95, 93, 97]],
    'tags': [['python', 'sql'], ['java'], ['python', 'rust', 'sql']]
})

# Work with list columns naturally
result = df.with_columns(
    # Average the scores in each list
    pl.col('scores').list.mean().alias('avg_score'),
    
    # Get the max score
    pl.col('scores').list.max().alias('best_score'),
    
    # Count tags
    pl.col('tags').list.len().alias('tag_count'),
    
    # Check if 'python' is in tags
    pl.col('tags').list.contains('python').alias('knows_python')
)

# Explode lists to long format (creates more ROWS)
df.explode('scores')  # Each score gets its own row
# Result:
# ┌─────────┬────────┬─────────────────────┐
# │ user    │ scores │ tags                │
# ├─────────┼────────┼─────────────────────┤
# │ Alice   │ 85     │ ['python', 'sql']   │
# │ Alice   │ 92     │ ['python', 'sql']   │
# │ Alice   │ 88     │ ['python', 'sql']   │
# │ Bob     │ 76     │ ['java']            │
# │ Bob     │ 81     │ ['java']            │
# │ Bob     │ 79     │ ['java']            │
# │ Charlie │ 95     │ ['python','rust'... │
# │ Charlie │ 93     │ ['python','rust'... │
# │ Charlie │ 97     │ ['python','rust'... │
# └─────────┴────────┴─────────────────────┘

# To create new COLUMNS from list positions (like a pivot):
df.with_columns(
    pl.col('scores').list.get(0).alias('score_1'),
    pl.col('scores').list.get(1).alias('score_2'),
    pl.col('scores').list.get(2).alias('score_3')
)
# Result:
# ┌─────────┬─────────────┬──────────────────┬─────────┬─────────┬─────────┐
# │ user    │ scores      │ tags             │ score_1 │ score_2 │ score_3 │
# ├─────────┼─────────────┼──────────────────┼─────────┼─────────┼─────────┤
# │ Alice   │ [85,92,88]  │ ['python','sql'] │ 85      │ 92      │ 88      │
# │ Bob     │ [76,81,79]  │ ['java']         │ 76      │ 81      │ 79      │
# │ Charlie │ [95,93,97]  │ ['python','rust..│ 95      │ 93      │ 97      │
# └─────────┴─────────────┴──────────────────┴─────────┴─────────┴─────────┘

# Classic pivot example - from long to wide format
sales_df = pl.DataFrame({
    'product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'],
    'sales': [100, 150, 120, 180, 130, 200]
})

# Pivot: rows become columns
sales_df.pivot(
    values='sales',
    index='product',
    columns='month'
)
# Result:
# ┌─────────┬─────┬─────┬─────┐
# │ product │ Jan │ Feb │ Mar │
# ├─────────┼─────┼─────┼─────┤
# │ A       │ 100 │ 120 │ 130 │
# │ B       │ 150 │ 180 │ 200 │
# └─────────┴─────┴─────┴─────┘

# Manipulate nested structures
df.with_columns(
    # Add 5 to each score in the list
    (pl.col('scores').list.eval(pl.element() + 5)).alias('curved_scores')
)
```

### The Power of Polars Expressions

Expressions are the heart of Polars - they're lazy, composable, and optimizable:

```python
# Expressions are recipes, not results
expr = pl.col('salary') * 1.1

# Use the same expression multiple times
df.select([
    expr.alias('new_salary'),
    expr.round(2).alias('rounded_salary'),
    (expr > 50000).alias('high_earner')
])

# Complex expressions with conditionals
df.with_columns(
    pl.when(pl.col('age') < 30)
    .then(pl.col('salary') * 1.2)
    .when(pl.col('age') < 50)
    .then(pl.col('salary') * 1.1)
    .otherwise(pl.col('salary') * 1.05)
    .alias('adjusted_salary')
)

# Expressions can be stored and reused
avg_by_dept = pl.col('salary').mean().over('department')
df.with_columns(
    avg_by_dept.alias('dept_avg'),
    (pl.col('salary') / avg_by_dept).alias('salary_ratio')
)
```

### String Operations: Fast and Expressive

```python
# String manipulation with expressions
df = pl.DataFrame({
    'email': ['john.doe@company.com', 'jane_smith@example.org', 'bob@test.io'],
    'full_name': ['John Doe', 'Jane Smith', 'Bob Johnson']
})

result = df.with_columns(
    # Extract domain from email
    pl.col('email').str.split('@').list.get(1).alias('domain'),
    
    # Extract username
    pl.col('email').str.split('@').list.get(0).alias('username'),
    
    # Convert to uppercase
    pl.col('full_name').str.to_uppercase().alias('name_upper'),
    
    # Extract first name
    pl.col('full_name').str.split(' ').list.get(0).alias('first_name'),
    
    # Check if email contains 'company'
    pl.col('email').str.contains('company').alias('is_company_email'),
    
    # Replace text
    pl.col('email').str.replace('@', ' AT ').alias('safe_email'),
    
    # String length
    pl.col('full_name').str.len_chars().alias('name_length')
)

# Regex support
df.with_columns(
    pl.col('email').str.extract(r'([^@]+)@([^.]+)\.(.+)', 1).alias('username_regex')
)

# String concatenation
df.with_columns(
    (pl.col('full_name') + ' <' + pl.col('email') + '>').alias('contact_info')
)
```

### More Complex Nested Operations

```python
# DataFrame with nested dictionaries/structs
df = pl.DataFrame({
    'id': [1, 2, 3],
    'metrics': [
        {'cpu': 45.2, 'memory': 78.5, 'disk': 23.1},
        {'cpu': 67.8, 'memory': 45.2, 'disk': 89.3},
        {'cpu': 23.4, 'memory': 91.2, 'disk': 45.6}
    ]
})

# Access struct fields
df.with_columns(
    pl.col('metrics').struct.field('cpu').alias('cpu_usage'),
    pl.col('metrics').struct.field('memory').alias('memory_usage')
)

# Working with nested lists of different lengths
df = pl.DataFrame({
    'student': ['Alice', 'Bob', 'Charlie'],
    'quiz_scores': [[8, 9, 7, 10], [6, 7], [9, 10, 10, 8, 9]]
})

df.with_columns(
    # Get statistics on variable-length lists
    pl.col('quiz_scores').list.mean().alias('avg_quiz'),
    pl.col('quiz_scores').list.std().alias('std_quiz'),
    pl.col('quiz_scores').list.slice(0, 3).list.mean().alias('first_three_avg')
)
```

---

## Resources to Continue Learning

- **The Fantastic Official Documentation**: [pola.rs](https://pola.rs) - Seriously, some of the best docs in the Python ecosystem
  - Clear examples for every method
  - Performance tips and best practices
  - Detailed migration guides from pandas
  
- **Polars User Guide**: [pola-rs.github.io/polars/user-guide](https://pola-rs.github.io/polars/user-guide)
  - In-depth explanations of concepts
  - Real-world use cases
  
- **API Reference**: [pola-rs.github.io/polars/py-polars/html/reference](https://pola-rs.github.io/polars/py-polars/html/reference)
  - Every function and method documented
  - Interactive examples you can run

- **Community Resources**:
  - Discord: Active community for questions
  - GitHub Discussions: Deep technical discussions
  - Stack Overflow: Growing collection of solutions

---

