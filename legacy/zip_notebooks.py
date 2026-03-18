#!/usr/bin/env python3
"""
Script to zip workshop notebooks part1 through part14
Creates a zip file containing all workshop notebook files
"""

import os
import zipfile
from datetime import datetime

def zip_notebooks():
    """Create a zip file containing all workshop notebooks"""
    
    # Define the notebooks directory and output zip file
    notebooks_dir = "notebooks"
    zip_filename = "notebooks.zip"
    
    # List of notebook files to include (part1 through part14)
    notebook_files = [
        "part1_colab.ipynb",
        "part2_objects.ipynb", 
        "part3_lists_dictionaries.ipynb",
        "part4_flow_control.ipynb",
        "part5_functions.ipynb",
        "part6_libraries.ipynb",
        "part7_pandas_intro.ipynb",
        "part8_pandas_more.ipynb",
        "part9_visualization_intro.ipynb",
        "part10_visualization_more.ipynb",
        "part11_visualization_plotly.ipynb",
        "part12_simulation.ipynb",
        "part13_goal_seek.ipynb",
        "part14_neural_networks.ipynb"
    ]
    
    # Create the zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        files_added = 0
        files_missing = 0
        
        print(f"Creating {zip_filename}...")
        print("-" * 50)
        
        for notebook in notebook_files:
            notebook_path = os.path.join(notebooks_dir, notebook)
            
            if os.path.exists(notebook_path):
                zipf.write(notebook_path, notebook)  # Add with just the filename in zip
                print(f"✓ Added: {notebook}")
                files_added += 1
            else:
                print(f"✗ Missing: {notebook}")
                files_missing += 1
        
        print("-" * 50)
        print(f"Summary:")
        print(f"  Files added: {files_added}")
        print(f"  Files missing: {files_missing}")
        print(f"  Zip file created: {zip_filename}")
        
        # Get zip file size
        zip_size = os.path.getsize(zip_filename)
        print(f"  Zip file size: {zip_size:,} bytes ({zip_size/1024:.1f} KB)")

if __name__ == "__main__":
    zip_notebooks()