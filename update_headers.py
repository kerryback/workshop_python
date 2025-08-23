#!/usr/bin/env python3
"""Update notebook headers to match part14 format"""

import json
import os

# Define notebook titles
notebook_titles = {
    'part3_lists_dictionaries.ipynb': 'Part 3: Lists and Dictionaries',
    'part4_flow_control.ipynb': 'Part 4: Flow Control', 
    'part5_functions.ipynb': 'Part 5: Functions',
    'part6_libraries.ipynb': 'Part 6: Libraries',
    'part7_pandas_intro.ipynb': 'Part 7: Introduction to Pandas',
    'part8_pandas_more.ipynb': 'Part 8: More Pandas',
    'part9_visualization_intro.ipynb': 'Part 9: Introduction to Visualization',
    'part10_visualization_more.ipynb': 'Part 10: More Visualization',
    'part11_visualization_plotly.ipynb': 'Part 11: Visualization with Plotly',
    'part12_simulation.ipynb': 'Part 12: Simulation',
    'part13_goal_seek.ipynb': 'Part 13: Goal Seek'
}

# Template cells
header_cells = [
    {
        "cell_type": "markdown",
        "id": "cell-0",
        "metadata": {},
        "source": "![](https://raw.githubusercontent.com/kerryback/workshop_python/main/images/mcnair.jpg)"
    },
    {
        "cell_type": "markdown", 
        "id": "cell-1",
        "metadata": {},
        "source": None  # Will be filled per notebook
    }
]

def update_notebook(filepath, title):
    """Update a notebook with new header cells"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Create title cell
        title_cell = {
            "cell_type": "markdown",
            "id": "cell-1", 
            "metadata": {},
            "source": f"---\n\n### JGSB Python Workshop {title}\n\n**Authored by Kerry Back, 09/06/2025**\n\n---\n\n"
        }
        
        # Replace first cell with image
        notebook['cells'][0] = {
            "cell_type": "markdown",
            "id": "cell-0",
            "metadata": {},
            "source": "![](https://raw.githubusercontent.com/kerryback/workshop_python/main/images/mcnair.jpg)"
        }
        
        # Insert title cell as second cell
        notebook['cells'].insert(1, title_cell)
        
        # Save the updated notebook
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        
        print(f"Updated: {filepath}")
        
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

# Update all notebooks
notebooks_dir = '/home/kerry/repos/workshop_python/notebooks'
for filename, title in notebook_titles.items():
    filepath = os.path.join(notebooks_dir, filename)
    if os.path.exists(filepath):
        update_notebook(filepath, title)
    else:
        print(f"File not found: {filepath}")

print("All notebooks updated!")