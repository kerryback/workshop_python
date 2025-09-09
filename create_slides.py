import os
import sys

notebooks = os.listdir("notebooks")
notebooks = [x.split(".")[0] for x in notebooks if x.endswith(".ipynb")]
for notebook in notebooks:
      with open(f"notebooks/{notebook}.ipynb", 'r') as f:
            contents = f.read()
            updated = contents.replace(
                  '"metadata": {}',
                  '"metadata": {"slideshow": {"slide_type": "slide"}}'
            )
      with open(f"notebooks/{notebook}.ipynb", 'w') as f:
            f.write(updated)
      os.system(f'jupyter nbconvert notebooks/{notebook}.ipynb --to slides --SlidesExporter.reveal_scroll=True')
      os.system(f"mv notebooks/{notebook}.slides.html docs/{notebook}.html")
#if flag:
#    os.system(f'decktape automatic docs\{notebook}.html docs\pdfs\{notebook}.pdf')