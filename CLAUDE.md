# Python Workshop Ver2 — Claude Instructions

## Rendering and Deploying Slides

When rendering `slides/python-overview.qmd` and committing changes, **always stage the theme CSS directory**:

```bash
git add docs/site_libs/revealjs/dist/theme/
```

Each time Quarto recompiles the SCSS (e.g. after any change to `slides/revealjs-style.scss`), it generates a **new hashed CSS filename** (e.g. `quarto-bd941f....css`). The HTML is updated to reference the new hash, but the new file must be explicitly added to git — otherwise GitHub Pages serves a 404 for the stylesheet and the slides lose all formatting.

**Commit pattern after any render:**
```bash
git add slides/python-overview.qmd
git add slides/revealjs-style.scss        # if changed
git add docs/slides/python-overview.html
git add docs/site_libs/revealjs/dist/theme/
git add docs/slides/files/                # if data files changed
```
