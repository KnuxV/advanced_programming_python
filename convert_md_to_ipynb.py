#!/usr/bin/env python3
"""
Markdown to Jupyter Notebook Converter

This script converts a markdown file containing code blocks into a Jupyter notebook.
Code blocks marked with ```python become code cells, everything else becomes markdown cells.

Usage:
    python convert.py input_file.md output_file.ipynb
"""

import nbformat
from pathlib import Path
import argparse
import sys


def convert_markdown_to_notebook(input_path: Path, output_path: Path) -> None:
    """
    Convert a markdown file to a Jupyter notebook.

    Args:
        input_path: Path to the input markdown file
        output_path: Path where the output notebook will be saved
    """

    # Read the markdown file content
    # Using UTF-8 encoding to handle any special characters properly
    try:
        markdown_text = input_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Could not read '{input_path}' as UTF-8 text.")
        sys.exit(1)

    # Initialize variables for cell parsing
    cells = []  # List to store all notebook cells
    current_lines = []  # Buffer to accumulate lines for the current cell
    cell_type = "markdown"  # Track whether we're in a markdown or code cell

    def flush_current_cell():
        """
        Helper function to process the accumulated lines and create a cell.
        This is called when we finish collecting lines for a cell.
        """
        # Access the module-level variables
        nonlocal current_lines, cell_type, cells

        # Skip empty cells
        if not current_lines:
            return

        # Join all lines and clean up extra newlines
        content = "\n".join(current_lines).strip("\n")

        # Create the appropriate cell type based on current context
        if cell_type == "code":
            # Create a code cell with no execution count or outputs
            # (these will be populated when the notebook is actually run)
            cell = nbformat.v4.new_code_cell(
                source=content,
                execution_count=None,  # Will be set when executed
                outputs=[]  # Will be populated when executed
            )
        else:
            # Create a markdown cell
            cell = nbformat.v4.new_markdown_cell(source=content)

        cells.append(cell)

        # Clear the buffer for the next cell
        current_lines = []

    # Parse the markdown text line by line
    for line in markdown_text.splitlines():

        # Check if this line starts a Python code block
        if line.strip().startswith("```python"):
            # Finish the current cell (likely markdown) before starting code
            flush_current_cell()
            cell_type = "code"
            # Don't include the ```python line in the code cell

        # Check if this line ends any code block
        elif line.strip().startswith("```") and not line.strip().startswith("```python"):
            # Finish the current code cell
            flush_current_cell()
            cell_type = "markdown"
            # Don't include the closing ``` line in the next markdown cell

        else:
            # This is a regular content line - add it to the current cell
            current_lines.append(line)

    # Don't forget to flush the last cell after processing all lines
    flush_current_cell()

    # Create the notebook structure
    # nbformat.v4 creates a notebook compatible with Jupyter notebook format version 4
    notebook = nbformat.v4.new_notebook(
        cells=cells,
        metadata={
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"  # You can adjust this
            }
        }
    )

    # Ensure the output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the notebook to disk
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            nbformat.write(notebook, f)
        print(f"✅ Notebook successfully saved to '{output_path}'")
        print(f"📊 Created {len(cells)} cells total")

        # Count cell types for user feedback
        code_cells = sum(1 for cell in cells if cell.cell_type == "code")
        markdown_cells = sum(1 for cell in cells if cell.cell_type == "markdown")
        print(f"   - {code_cells} code cells")
        print(f"   - {markdown_cells} markdown cells")

    except Exception as e:
        print(f"Error: Could not write to '{output_path}': {e}")
        sys.exit(1)


def main():
    """
    Main function that handles command line arguments and orchestrates the conversion.
    """
    # Set up argument parser for command line interface
    parser = argparse.ArgumentParser(
        description="Convert a markdown file with code blocks to a Jupyter notebook",
        epilog="Example: python convert.py my_tutorial.md my_notebook.ipynb"
    )

    parser.add_argument(
        "input_path",
        type=str,
        help="Path to the input markdown file"
    )

    parser.add_argument(
        "output_path",
        type=str,
        help="Path for the output Jupyter notebook file"
    )

    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Overwrite output file if it already exists"
    )

    # Parse command line arguments
    args = parser.parse_args()

    # Convert string paths to Path objects for better path handling
    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    # Validate input file exists
    if not input_path.exists():
        print(f"❌ Error: Input file '{input_path}' does not exist.")
        sys.exit(1)

    if not input_path.is_file():
        print(f"❌ Error: '{input_path}' is not a file.")
        sys.exit(1)

    # Check if output file already exists
    if output_path.exists() and not args.force:
        response = input(f"Output file '{output_path}' already exists. Overwrite? (y/n): ")
        if response.lower() not in ['y', 'yes']:
            print("Operation cancelled.")
            sys.exit(0)

    # Ensure output has .ipynb extension
    if output_path.suffix.lower() != '.ipynb':
        print(f"⚠️  Warning: Output file should have .ipynb extension")
        response = input("Continue anyway? (y/n): ")
        if response.lower() not in ['y', 'yes']:
            sys.exit(0)

    print(f"🔄 Converting '{input_path}' to '{output_path}'...")

    # Perform the conversion
    convert_markdown_to_notebook(input_path, output_path)


if __name__ == "__main__":
    main()