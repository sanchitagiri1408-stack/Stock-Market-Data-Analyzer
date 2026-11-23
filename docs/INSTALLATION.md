# 💻 Installation Guide

## Prerequisites

- Python 3.10+ (check: `python --version`)
- pip (check: `pip --version`)
- Git (check: `git --version`)

---

## Step 1 — Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Stock-Market-Data-Analyzer.git
cd Stock-Market-Data-Analyzer
```

---

## Step 2 — Create a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal prompt.

---

## Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

This installs: pandas, numpy, matplotlib, seaborn, yfinance, streamlit, plotly.

---

## Step 4 — Verify installation

```bash
python main.py --help
```

You should see the help text with `--ticker`, `--start`, `--end`, `--csv`, etc.

---

## Step 5 — Run the project

```bash
python main.py
```

Wait ~10 seconds. The console will print a summary and the `outputs/` folder
will contain charts and reports.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: yfinance` | `pip install yfinance` |
| `No module named pandas` | `pip install pandas` |
| `Permission denied` (Mac/Linux) | `chmod +x main.py` or use `python3` |
| `streamlit: command not found` | `pip install streamlit` then `streamlit run dashboard.py` |
| yfinance returns empty | Ticker may be delisted; try AAPL, MSFT, GOOGL |

---

## Windows-specific notes

- Use `venv\Scripts\activate` (not `source venv/bin/activate`)
- If PowerShell blocks scripts: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
- Use `python` not `python3` on most Windows installs

---

## Mac-specific notes

- Use `python3` not `python`
- If you get Xcode errors: `xcode-select --install`
- Consider `brew install python` for latest version

---

*Educational project. Not financial advice.*
