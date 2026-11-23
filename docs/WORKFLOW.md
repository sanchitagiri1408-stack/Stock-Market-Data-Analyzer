# 🔄 Project Workflow

This document explains the end-to-end workflow of the Stock Market Data Analyzer.

---

## High-Level Pipeline

```
┌─────────────────┐
│  INPUT          │
│  - Ticker       │
│  - Date range   │
│  - CSV path     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  DATA COLLECTION│
│  - yfinance     │
│  - CSV fallback │
│  - Synthetic    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  DATA CLEANING  │
│  - Drop NaN     │
│  - Dedupe dates │
│  - Sort by date │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ANALYSIS       │
│  - Daily return │
│  - SMA 20/50/200│
│  - Volatility   │
│  - Sharpe       │
│  - Max DD       │
│  - Trend        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  VISUALIZATION  │
│  - 9 charts     │
│  - PNG output   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  REPORT         │
│  - Text report  │
│  - Markdown     │
│  - Console      │
└─────────────────┘
```

---

## Step-by-Step Explanation

### 1. Input
The user provides:
- **Ticker symbol** (e.g., AAPL, MSFT, RELIANCE.NS)
- **Date range** (start, end)
- Optional **CSV path** for offline data

### 2. Data Collection
`data_loader.py` tries three sources in order:
1. **yfinance** — live data from Yahoo Finance
2. **CSV file** — pre-downloaded data
3. **Synthetic** — Geometric Brownian Motion simulation

This ensures the tool works even without internet.

### 3. Data Cleaning
- Remove rows with missing OHLCV values
- Remove duplicate dates
- Sort by date ascending
- Reset index

### 4. Analysis
`analyzer.py` computes:
- **Daily returns** — `pct_change()`
- **Cumulative returns** — `(P_t / P_0) - 1`
- **Moving averages** — `rolling(window).mean()`
- **Volatility** — `rolling(window).std()`
- **Sharpe ratio** — risk-adjusted return
- **Max drawdown** — worst peak-to-trough loss
- **Trend** — SMA 50 vs SMA 200 crossover
- **Support/Resistance** — 25th/75th percentiles

### 5. Visualization
`visualization.py` generates 9 charts:
1. Price with moving averages
2. Daily returns distribution (histogram + KDE)
3. Cumulative returns
4. Rolling volatility
5. Volume bar chart
6. High-Low range with close
7. Monthly returns heatmap
8. Drawdown over time
9. Return vs Volume scatter

### 6. Report
`report.py` produces:
- **Text report** — human-readable, plain English
- **Markdown report** — for GitHub/wiki
- **Console summary** — printed at end of run

---

## Data Flow Diagram

```
User CLI args
     │
     ▼
main.py (argparse)
     │
     ▼
data_loader.load_data() ──► DataFrame (raw)
     │
     ▼
Cleaning (dropna, dedupe, sort)
     │
     ▼
analyzer.run_full_analysis() ──► DataFrame (enriched)
     │
     ▼
visualization.generate_all_charts() ──► 9 PNG files
     │
     ▼
analyzer.compute_summary() ──► dict of metrics
     │
     ▼
report.generate_text_report() ──► .txt file
report.generate_markdown_report() ──► .md file
     │
     ▼
Console output (summary table)
```

---

## Why This Workflow?

| Stage | Why it matters |
|---|---|
| Collection | Real data is the foundation; fallback ensures reliability |
| Cleaning | Garbage in = garbage out; analysis is only as good as data |
| Analysis | Transforms raw prices into actionable metrics |
| Visualization | Humans understand charts faster than tables |
| Report | Communicates findings to non-technical stakeholders |

---

*Educational project only. Not financial advice.*
