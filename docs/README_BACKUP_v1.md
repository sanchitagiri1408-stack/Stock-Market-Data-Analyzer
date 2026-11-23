# 📈 Stock Market Data Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green?style=flat&logo=pandas)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)

> A beginner-friendly, modular Python project that fetches stock market data,
> analyses price trends, computes risk metrics, and generates professional
> charts and reports — all from public data sources.

---

## 📌 Project Overview

The **Stock Market Data Analyzer** is a complete Python application that:

1. **Fetches** stock data from Yahoo Finance (or falls back to CSV / synthetic data)
2. **Cleans** the dataset (handles missing values, duplicates, sorting)
3. **Analyses** price movement (daily returns, moving averages, volatility)
4. **Visualises** trends with 9 professional charts
5. **Reports** insights in plain English (text + Markdown)

It is built as a **course project** and designed as **proof of work** for
GitHub — suitable for Python Developer, Data Analyst, Financial Analyst,
Business Analyst, and FinTech roles.

---

## ⚠️ Disclaimer

> **This project is for EDUCATIONAL PURPOSES ONLY.**
> It is **NOT financial advice**. Do not use it to make investment decisions.
> Always consult a licensed financial advisor before investing.

---

## 🎯 Problem Statement

Students and junior analysts often lack access to expensive financial terminals
(Bloomberg, Reuters Eikon). This project demonstrates how to build a working
stock analysis tool using **only free, public data** and open-source Python
libraries — proving skills in data engineering, analysis, and visualisation.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 📥 **Data Fetching** | yfinance API with CSV + synthetic fallback |
| 🧹 **Data Cleaning** | Handles missing values, duplicates, date sorting |
| 📊 **Daily Returns** | Percentage change of closing prices |
| 📈 **Moving Averages** | SMA 20 / 50 / 200 for trend detection |
| 📉 **Volatility** | Rolling 20-day std dev of returns |
| ⚖️ **Risk Metrics** | Sharpe ratio, max drawdown, annualised return |
| 🎨 **9 Charts** | Price, returns distribution, cumulative returns, volatility, volume, high-low range, monthly heatmap, drawdown, return-vs-volume |
| 📝 **Auto Report** | Text + Markdown report with plain-English interpretation |
| 🖥️ **Dashboard** | Optional Streamlit interactive dashboard |

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Language | Python 3.10+ |
| Data | pandas, numpy |
| Viz | matplotlib, seaborn |
| Data Source | yfinance (optional) |
| Dashboard | streamlit (optional) |
| Notebook | Jupyter (optional) |

---

## 📁 Folder Structure

```
Stock-Market-Data-Analyzer/
│
├── data/
│   ├── raw/              # Raw downloaded CSVs (git-ignored)
│   └── processed/        # Cleaned data (git-ignored)
│
├── notebooks/            # Jupyter exploration notebooks
│
├── src/                  # Core source code
│   ├── __init__.py
│   ├── data_loader.py    # Fetch / load / fallback logic
│   ├── analyzer.py       # Returns, MAs, volatility, risk metrics
│   ├── visualization.py  # All chart functions
│   └── report.py         # Text + Markdown report generation
│
├── outputs/
│   ├── charts/           # Generated PNG charts (git-ignored)
│   └── *.csv             # Processed data export
│
├── images/               # Screenshots for README
│
├── reports/              # Final reports (git-ignored)
│
├── docs/                 # Extra documentation
│
├── main.py               # CLI entry point
├── dashboard.py          # Streamlit dashboard (optional)
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Stock-Market-Data-Analyzer.git
cd Stock-Market-Data-Analyzer
```

### 2. Create a virtual environment

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

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Basic usage (default: AAPL, 2023-01-01 to 2024-12-31)

```bash
python main.py
```

### Custom ticker and date range

```bash
python main.py --ticker MSFT --start 2022-01-01 --end 2023-01-01
```

### Use a local CSV file

```bash
python main.py --ticker AAPL --csv data/sample_aapl.csv
```

### Launch the Streamlit dashboard

```bash
streamlit run dashboard.py
```

---

## 📊 Sample Output

After running, the console prints a summary like:

```
=================================================================
  ANALYSIS SUMMARY
=================================================================
  Ticker........................ AAPL
  Date Range.................... 2023-01-02 to 2024-12-31
  Trading Days.................. 522
  Start Price................... 150.60
  End Price..................... 223.83
  Total Return (%).............. 48.63
  Annualised Volatility (%)..... 24.98
  Sharpe Ratio (rf=0%).......... 0.8923
  Max Drawdown (%).............. -30.25
  Trend (SMA 50 vs 200)......... Downtrend
=================================================================
```

And the `outputs/` folder will contain:

- `AAPL_analysis_report.txt` — human-readable report
- `AAPL_analysis_report.md`  — Markdown report
- `AAPL_processed_data.csv`  — enriched dataset
- `charts/AAPL_*.png`        — 9 chart images

---

## 📸 Screenshots

See the [`images/`](images/) folder for:

- Project folder structure
- Sample dataset preview
- Terminal output
- Closing price chart
- Moving average chart
- Daily returns distribution
- Volatility chart
- Final report output
- GitHub repository preview

---

## 📚 Learning Outcomes

By building this project you will learn:

- ✅ Working with financial APIs (yfinance)
- ✅ Data cleaning with pandas
- ✅ Financial calculations (returns, volatility, Sharpe, drawdown)
- ✅ Technical analysis (moving averages, support/resistance, trend)
- ✅ Data visualisation with matplotlib & seaborn
- ✅ Modular Python project structure
- ✅ CLI argument parsing with argparse
- ✅ Report generation (text + Markdown)
- ✅ Git / GitHub workflow
- ✅ Optional: Streamlit dashboards

---

## 🧪 Project Workflow

```
Stock Data Collection → Data Cleaning → Price Trend Analysis →
Moving Averages → Returns Calculation → Risk Analysis →
Visualization → Report Generation
```

---

## 🤝 Contributing

This is a student course project. Feel free to fork and extend it.

---

## 📄 License

MIT License — see `LICENSE` file.

---

## 🙏 Acknowledgements

- [yfinance](https://github.com/ranaroussi/yfinance) for free market data
- [pandas](https://pandas.pydata.org/), [matplotlib](https://matplotlib.org/),
  [seaborn](https://seaborn.pydata.org/) for analysis & viz
- The Python community for excellent open-source tooling

---

*Built with ❤️ by a student, for learning purposes.*
