# 🔧 GitHub Upload — Complete Step-by-Step Guide

This guide walks you through pushing the Stock Market Data Analyzer to GitHub
and making it look professional.

---

## 1️⃣ Create the Repository

1. Go to <https://github.com> and sign in.
2. Click the **+** icon (top-right) → **New repository**.
3. Fill in:
   - **Repository name:** `Stock-Market-Data-Analyzer`
   - **Description:** `Automated Python tool for stock price analysis using yfinance, pandas & matplotlib. Computes returns, moving averages, volatility, Sharpe ratio, and generates charts & reports.`
   - **Visibility:** Public
   - **Do NOT** initialise with README, .gitignore, or license (we already have these).
4. Click **Create repository**.

---

## 2️⃣ Best Repository Metadata

| Field | Value |
|---|---|
| **Repo name** | `Stock-Market-Data-Analyzer` |
| **Description** | `Automated Python tool for stock price analysis using yfinance, pandas & matplotlib. Computes returns, moving averages, volatility, Sharpe ratio, and generates charts & reports.` |
| **Topics / Tags** | `python`, `stock-market`, `data-analysis`, `finance`, `pandas`, `matplotlib`, `yfinance`, `financial-analysis`, `data-visualization`, `fintech`, `student-project`, `course-project` |

---

## 3️⃣ Connect Local Folder to GitHub

Open a terminal in the project folder and run:

```bash
# 1. Initialise a git repo
git init

# 2. Add all files
git add .

# 3. First commit
git commit -m "feat: initial commit - stock market data analyzer"

# 4. Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Stock-Market-Data-Analyzer.git

# 5. Rename branch to main
git branch -M main

# 6. Push to GitHub
git push -u origin main
```

---

## 4️⃣ Recommended Commit Sequence

If you want clean history, commit in stages:

```bash
git add requirements.txt .gitignore
git commit -m "chore: add project setup files"

git add src/
git commit -m "feat: add data loader, analyzer, visualization & report modules"

git add main.py dashboard.py
git commit -m "feat: add CLI entry point and Streamlit dashboard"

git add data/sample_aapl.csv
git commit -m "docs: add sample CSV for offline fallback demo"

git add README.md
git commit -m "docs: add comprehensive README"

git add outputs/reports/
git commit -m "docs: add sample analysis outputs and charts"

git push -u origin main
```

---

## 5️⃣ Commit Message Convention

Use conventional commits for a professional look:

| Type | Meaning | Example |
|---|---|---|
| `feat:` | New feature | `feat: add moving average crossover signal` |
| `fix:` | Bug fix | `fix: handle missing Close prices in returns calc` |
| `docs:` | Documentation | `docs: update README with output examples` |
| `refactor:` | Code cleanup | `refactor: split analyzer into smaller functions` |
| `chore:` | Maintenance | `chore: bump yfinance to 0.2.40` |
| `test:` | Add tests | `test: add unit tests for Sharpe ratio calc` |

---

## 6️⃣ Screenshots to Upload

Save these into the `images/` folder and reference them in README.md:

| Screenshot | What to capture |
|---|---|
| `folder-structure.png` | VS Code explorer showing project tree |
| `dataset-preview.png` | `df.head()` output in terminal |
| `terminal-output.png` | Full `python main.py` run |
| `price-chart.png` | AAPL_price_moving_avg.png |
| `returns-dist.png` | AAPL_returns_distribution.png |
| `moving-avg-chart.png` | Chart with SMA 20/50/200 |
| `volatility-chart.png` | AAPL_volatility.png |
| `final-report.png` | Open `AAPL_analysis_report.txt` |
| `github-repo.png` | GitHub repo page screenshot |
| `dashboard.png` | Streamlit dashboard in browser |

To embed in README, use:

```markdown
![Folder Structure](images/folder-structure.png)
![Terminal Output](images/terminal-output.png)
```

---

## 7️⃣ Make It Look Professional

1. **Add a LICENSE file:**
   ```bash
   # Create MIT license
   echo "MIT License

   Copyright (c) 2026 YOUR_NAME

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files..." > LICENSE
   git add LICENSE
   git commit -m "chore: add MIT license"
   ```

2. **Add topics** on GitHub repo page (About → ⚙️ → Topics).

3. **Pin the repository** on your GitHub profile (Profile → Customise profile → Pin repositories).

4. **Add a project description** at the top of the profile README.

---

## 8️⃣ Day-by-Day Proof Building Strategy

| Day | What to do | Commit message | Screenshot |
|---|---|---|---|
| **Day 1** | Setup virtual env, folders, requirements | `chore: project setup` | Folder structure |
| **Day 2** | Implement data_loader.py, test fetch | `feat: data fetching module` | Dataset preview |
| **Day 3** | Data cleaning + EDA | `feat: cleaning & EDA` | Head/tail output |
| **Day 4** | Moving averages + returns analysis | `feat: returns & MAs` | Price chart |
| **Day 5** | Volatility + risk metrics | `feat: volatility & Sharpe ratio` | Volatility chart |
| **Day 6** | Visualization + report generation | `feat: charts & reports` | Report screenshot |
| **Day 7** | README + GitHub polish | `docs: complete README & screenshots` | GitHub repo page |

---

## 9️⃣ Sample .gitignore (already included)

See `.gitignore` in the project root. Key rules:

- `data/raw/*.csv` — don't track large downloaded files
- `outputs/charts/*.png` — don't track generated images
- `reports/*.txt` — don't track generated reports
- `venv/`, `__pycache__/` — Python artifacts

---

## 🔟 Final Checklist Before Pushing

- [ ] `README.md` complete with badges and instructions
- [ ] `LICENSE` file added
- [ ] `requirements.txt` matches actual dependencies
- [ ] `.gitignore` excludes venv/ and generated files
- [ ] `main.py --help` works
- [ ] `python main.py` runs without errors
- [ ] Sample outputs committed (or documented how to generate)
- [ ] Repo description and topics set on GitHub
- [ ] Repository pinned on profile

---

<https://github.com/YOUR_USERNAME/Stock-Market-Data-Analyzer>
