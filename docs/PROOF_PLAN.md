# 📅 Day-by-Day Proof Building Strategy (6 Days)

Use this plan to build the project progressively while committing to Git each day.
Each commit becomes visible proof of your work on GitHub.

---

## 🗓️ Day 1 — Project Setup

**Goal:** Create the skeleton of the project.

**What to do:**
- Create GitHub repo `Stock-Market-Data-Analyzer`
- Clone locally
- Create folder structure (data, src, notebooks, outputs, images, reports, docs)
- Write `requirements.txt` and `.gitignore`
- Add `README.md` with project title, badges, disclaimer

**Commit message:**
```
chore: initial project structure with README and setup files
```

**Screenshot:** Project folder in VS Code explorer.

---

## 🗓️ Day 2 — Stock Data Fetching

**Goal:** Get real stock data into Python.

**What to do:**
- Write `src/data_loader.py` with `fetch_from_yfinance()`, `load_from_csv()`, `generate_sample_data()`
- Test with AAPL, MSFT, GOOGL
- Save a sample CSV in `data/raw/`

**Commit message:**
```
feat: add data loader with yfinance and CSV fallback
```

**Screenshot:** `df.head()` output in terminal.

---

## 🗓️ Day 3 — Data Cleaning & EDA

**Goal:** Make the data trustworthy.

**What to do:**
- Add cleaning steps (dropna, dedupe, sort)
- Compute basic stats: mean, median, min, max, std
- Print summary to console

**Commit message:**
```
feat: add data cleaning and exploratory analysis
```

**Screenshot:** Terminal output showing "Removed X rows" and stats.

---

## 🗓️ Day 4 — Moving Averages & Returns

**Goal:** Compute the core financial metrics.

**What to do:**
- Write `src/analyzer.py`
- Add `compute_daily_returns()`, `compute_cumulative_returns()`, `compute_moving_averages()`
- Add `compute_volatility()`, `sharpe_ratio()`, `max_drawdown()`

**Commit message:**
```
feat: implement returns, moving averages, and risk metrics
```

**Screenshot:** DataFrame with SMA_20, SMA_50, SMA_200 columns.

---

## 🗓️ Day 5 — Visualization

**Goal:** Turn numbers into charts.

**What to do:**
- Write `src/visualization.py`
- Generate 9 charts:
  - Price with MAs
  - Returns distribution
  - Cumulative returns
  - Volatility
  - Volume
  - High-Low range
  - Monthly returns heatmap
  - Drawdown
  - Return vs Volume

**Commit message:**
```
feat: add 9 professional charts for analysis
```

**Screenshot:** Grid of chart PNGs.

---

## 🗓️ Day 6 — Report & GitHub Documentation

**Goal:** Ship a polished project.

**What to do:**
- Write `src/report.py` (text + Markdown report)
- Write `main.py` CLI entry point
- Add `dashboard.py` Streamlit dashboard (bonus)
- Finalise README with sample outputs and screenshots
- Add `docs/GITHUB_SETUP.md`, `docs/INTERVIEW_PREP.md`
- Push to GitHub

**Commit message:**
```
feat: add report generation, CLI, and final documentation
```

**Screenshot:** GitHub repo page with README rendered.

---

## ✅ Final Checklist

- [ ] All 6 days committed
- [ ] README has badges, instructions, screenshots
- [ ] Repo has topics/tags
- [ ] LICENSE file added
- [ ] Repo pinned on profile
- [ ] `python main.py` runs without errors
- [ ] All charts generated
- [ ] Report saved

---

*This project is for EDUCATIONAL PURPOSES ONLY. Not financial advice.*
