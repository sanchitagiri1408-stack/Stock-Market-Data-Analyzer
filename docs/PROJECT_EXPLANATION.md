# 📖 Project Explanation — Stock Market Data Analyzer

---

## What is a Stock Market Data Analyzer?

### Simple explanation

Imagine you have a notebook where you write down the price of a company's
shares every day. After a year, you have 250+ numbers. A Stock Market Data
Analyzer is a program that reads those numbers and tells you:

- Did the price go up or down overall?
- How much did it swing day-to-day?
- Is it trending up, down, or sideways?
- How risky is it?

Instead of reading hundreds of numbers yourself, the computer does the math
and draws charts so you can see the story at a glance.

### Technical explanation

A Stock Market Data Analyzer is a Python application that:

1. **Ingests** time-series OHLCV data (Open, High, Low, Close, Volume) from
   a public API (Yahoo Finance via `yfinance`) or a local CSV file.
2. **Cleans** the data (handles missing values, duplicates, sorting).
3. **Computes** financial metrics:
   - Daily returns: `r_t = P_t / P_{t-1} - 1`
   - Cumulative returns: `CR_t = P_t / P_0 - 1`
   - Simple Moving Averages: `SMA_n = (1/n) Σ P_i` over window n
   - Volatility: rolling std dev of returns, annualised × √252
   - Sharpe ratio: `(mean_return - rf) / std_return × √252`
   - Max drawdown: `min(P_t / cummax(P_t) - 1)`
4. **Visualises** the metrics with matplotlib/seaborn.
5. **Reports** findings in plain English.

---

## What problem does it solve?

| Problem | How this project solves it |
|---|---|
| Expensive terminals (Bloomberg, Reuters) | Uses free Yahoo Finance data |
| Manual analysis is slow | Automated pipeline in seconds |
| Hard to compare stocks | Same metrics for any ticker |
| Charts are hard to make | 9 professional charts auto-generated |
| Reports take hours | Auto-generated text + Markdown |

---

## Who uses this?

- **Investors** — assess risk before buying
- **Analysts** — quick screening of stocks
- **Traders** — identify trends via moving averages
- **Finance teams** — track portfolio performance
- **Students** — learn financial data analysis

---

## How companies use stock data analysis

1. **Investment research** — analysts screen thousands of stocks for opportunities
2. **Market tracking** — monitor indices, sectors, competitors
3. **Trend analysis** — identify momentum, reversals, seasonality
4. **Risk management** — measure volatility, drawdown, VaR
5. **Decision-making** — buy/sell/hold signals from technical indicators

---

## How Python can analyse stock price movement

Python's ecosystem makes financial analysis accessible:

- **pandas** — time-series manipulation, rolling windows, pct_change
- **numpy** — fast numerical computation (std, mean, sqrt)
- **matplotlib/seaborn** — publication-quality charts
- **yfinance** — free market data
- **scikit-learn** (optional) — predictive models

Example: computing a 20-day moving average

```python
df['SMA_20'] = df['Close'].rolling(window=20).mean()
```

---

## Workflow

```
Stock data collection
        ↓
   Data cleaning
        ↓
 Price trend analysis
        ↓
  Moving averages
        ↓
 Returns calculation
        ↓
   Risk analysis
        ↓
  Visualization
        ↓
Report generation
```

Each stage is a separate module in this project:

| Stage | Module |
|---|---|
| Collection | `src/data_loader.py` |
| Cleaning | `main.py` (step 2) |
| Analysis | `src/analyzer.py` |
| Visualization | `src/visualization.py` |
| Report | `src/report.py` |

---

*Educational project. Not financial advice.*
