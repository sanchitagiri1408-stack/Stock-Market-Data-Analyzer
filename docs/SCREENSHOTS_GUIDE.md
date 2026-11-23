# 📸 Screenshots & Outputs Guide

This document tells you **exactly** what to capture for your GitHub repo.

---

## Screenshots to capture

### 1. Project folder screenshot
- **What:** VS Code Explorer showing the full folder tree
- **How:** Open project in VS Code → expand folders → screenshot
- **Save as:** `images/folder-structure.png`

### 2. Stock dataset preview
- **What:** `df.head()` output in terminal or Jupyter
- **How:** Run `python main.py --ticker AAPL` and screenshot the loaded rows
- **Save as:** `images/dataset-preview.png`

### 3. Terminal output
- **What:** Full console output of `python main.py`
- **How:** Run the command, scroll to top, screenshot entire terminal
- **Save as:** `images/terminal-output.png`

### 4. Stock closing price chart
- **What:** `outputs/charts/AAPL_price_moving_avg.png`
- **How:** Open the PNG in an image viewer, screenshot
- **Save as:** `images/price-chart.png`

### 5. Moving average chart
- **What:** Same chart zoomed on the SMA lines
- **How:** Crop the price chart to focus on SMA_20/50/200
- **Save as:** `images/moving-avg-chart.png`

### 6. Daily returns chart
- **What:** `outputs/charts/AAPL_returns_distribution.png`
- **How:** Open PNG, screenshot
- **Save as:** `images/returns-dist.png`

### 7. Volatility summary
- **What:** `outputs/charts/AAPL_volatility.png`
- **How:** Open PNG, screenshot
- **Save as:** `images/volatility-chart.png`

### 8. Final report output
- **What:** Open `outputs/AAPL_analysis_report.txt` in a text editor
- **How:** Screenshot the full report
- **Save as:** `images/final-report.png`

### 9. GitHub repo preview
- **What:** Your GitHub repository page with README rendered
- **How:** Open repo in browser → screenshot
- **Save as:** `images/github-repo.png`

### 10. Dashboard screenshot (bonus)
- **What:** Streamlit dashboard running in browser
- **How:** `streamlit run dashboard.py` → screenshot browser
- **Save as:** `images/dashboard.png`

---

## How to embed in README

```markdown
![Folder Structure](images/folder-structure.png)
![Terminal Output](images/terminal-output.png)
![Price Chart](images/price-chart.png)
![Returns Distribution](images/returns-dist.png)
![Volatility Chart](images/volatility-chart.png)
![Final Report](images/final-report.png)
![GitHub Repo](images/github-repo.png)
```

---

## Tips for professional screenshots

1. **Use a clean terminal theme** — dark mode looks professional
2. **Hide sensitive info** — blur usernames, paths, API keys
3. **Crop tightly** — remove unnecessary whitespace
4. **Consistent naming** — use kebab-case for filenames
5. **Add captions** — in README, describe each image

---

*Educational project. Not financial advice.*
