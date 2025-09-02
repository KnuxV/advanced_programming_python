import nbformat
from pathlib import Path

# Path to your output notebook
output_path = Path("code-examples/05-polars_vs_pandas.ipynb")

# Load your markdown text (paste it as a string)
markdown_text = Path("code-examples/05-polars_vs_pandas.md").read_text(encoding="utf-8")

# Split into cells: code vs markdown
cells = []
current_lines = []
cell_type = "markdown"

def flush():
    global current_lines, cell_type
    if not current_lines:
        return
    content = "\n".join(current_lines).strip("\n")
    if cell_type == "code":
        cells.append(nbformat.v4.new_code_cell(content, execution_count=None, outputs=[]))
    else:
        cells.append(nbformat.v4.new_markdown_cell(content))
    current_lines = []

for line in markdown_text.splitlines():
    if line.strip().startswith("```python"):
        flush()
        cell_type = "code"
        current_lines = []
    elif line.strip().startswith("```"):
        flush()
        cell_type = "markdown"
        current_lines = []
    else:
        current_lines.append(line)

flush()

# Build the notebook
nb = nbformat.v4.new_notebook(cells=cells, metadata={"language": "python"})

# Write the notebook
with open(output_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Notebook saved to {output_path}")
