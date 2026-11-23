# 🎯 Interview Preparation — Stock Market Data Analyzer

---

## 1️⃣ "Explain your project."

**Strong answer:**

"I built a Stock Market Data Analyzer in Python. It fetches historical stock
data using yfinance from Yahoo Finance — or falls back to a CSV file if there's
no internet access. The pipeline cleans the data, computes daily returns,
cumulative returns, moving averages (SMA 20/50/200), rolling volatility, Sharpe
ratio, max drawdown, and identifies trends. It then generates 9 professional
charts and a text + markdown report with plain-English interpretation. The
project is modular — data loading, analysis, visualisation, and reporting are
separate modules — with a CLI entry point and an optional Streamlit dashboard.
I built it as a course project to demonstrate skills relevant to data analyst,
Python developer, and FinTech roles."

**Follow-up questions to expect:**
- Why Python instead of Excel?
- How does yfinance work?
- What is the Sharpe ratio?

---

## 2️⃣ "What problem does this solve?"

**Answer:**

"Retail investors and finance students don't have access to Bloomberg
terminals. This tool uses free, public data to produce the same core analyses —
trend detection, risk assessment, return distribution, drawdown analysis — in
an automated, reproducible way. It's also a learning vehicle: understanding
*how* these calculations work makes you a better analyst than just reading
numbers off a screen."

---

## 3️⃣ "How do you fetch the data?"

**Answer:**

"I use the yfinance library, which scrapes Yahoo Finance's public endpoints
(unofficially, but reliably). In code:

```python
import yfinance as yf
df = yf.download('AAPL', start='2023-01-01', end='2024-12-31')
```

yfinance returns OHLCV data (Open, High, Low, Close, Volume) plus Adj Close.
I structured data_loader.py with a fallback chain: try yfinance → try local
CSV → generate synthetic data using Geometric Brownian Motion. This makes the
tool robust to network failures."

---

## 4️⃣ "How does yfinance work under the hood?"

**Answer:**

"yfinance makes HTTP requests to Yahoo Finance's query endpoints and parses
the JSON response into a pandas DataFrame. It doesn't require an API key for
basic usage, but is subject to Yahoo's rate limits. For production use with
heavy workloads, you'd switch to an official API like Alpha Vantage, Twelve
Data, or Polygon.io."

---

## 5️⃣ "How do you clean the data?"

**Answer:**

"I apply three steps:

1. Drop rows with missing Open/High/Low/Close/Volume — financial time series
   can't have holes in critical fields.
2. Remove duplicate dates — sometimes data providers return overlapping rows.
3. Sort by date ascending — ensures rolling calculations (SMA, volatility)
   are computed correctly."

---

## 6️⃣ "What is a moving average and why is it useful?"

**Answer:**

"A Simple Moving Average (SMA) is the average price over a rolling window —
e.g., SMA-20 is the average of the last 20 closing prices. Traders use it to
smooth out noise and identify trend direction:

- Price above SMA = bullish
- Price below SMA = bearish
- SMA-20 crossing above SMA-50 = Golden Cross (uptrend signal)
- SMA-20 crossing below SMA-50 = Death Cross (downtrend signal)

In my code: `df['SMA_20'] = df['Close'].rolling(window=20).mean()`"

---

## 7️⃣ "How do you calculate daily returns?"

**Answer:**

"Daily return = (P_today / P_yesterday) - 1. Using pandas:

```python
df['Daily_Return'] = df['Close'].pct_change()
```

Returns are preferred over raw prices for several analyses because they're
stationary (statistical properties don't change over time), additive across
time for log returns, and comparable across stocks with different price levels."

---

## 8️⃣ "What is volatility and how do you compute it?"

**Answer:**

"Volatility measures the dispersion of returns — it's essentially the standard
deviation. I compute rolling 20-day volatility, then annualise it:

```python
df['Volatility'] = df['Daily_Return'].rolling(20).std()
annual_vol = df['Daily_Return'].std() * np.sqrt(252)  # 252 trading days
```

High volatility = high risk (large price swings). Low volatility = stable
stock. Annualised volatility of 25% means the stock typically swings ~25% per
year."

---

## 9️⃣ "What is the Sharpe ratio?"

**Answer:**

"The Sharpe ratio measures risk-adjusted return:

Sharpe = (Mean Return - Risk-Free Rate) / Std Dev of Returns × √(252)

Interpretation:
- > 1.5: Excellent
- 1.0 – 1.5: Good
- 0.5 – 1.0: Acceptable
- < 0.5: Poor

In my code: `sharpe_ratio = (returns.mean() - rf/252) / returns.std() * np.sqrt(252)`"

---

## 🔟 "What is maximum drawdown?"

**Answer:**

"Max drawdown is the largest peak-to-trough decline in the price series. It
tells you the worst-case loss an investor would have experienced.

```python
rolling_max = prices.cummax()
drawdown = prices / rolling_max - 1
max_dd = drawdown.min()
```

A max drawdown of -30% means at some point, the stock fell 30% from its
highest point before recovering (or not)."

---

## Bonus: "What would you improve if you had more time?"

**Answer:**

"Three things:
1. Add backtesting of SMA crossover strategies to measure actual profitability
2. Integrate a proper database (PostgreSQL) instead of CSV
3. Add portfolio-level analysis (correlation, diversification, equal-weight vs
   optimisation)
4. Deploy the Streamlit dashboard to Streamlit Cloud or as a Docker container
5. Add unit tests with pytest"

---

## 📌 HR vs Technical Explanation

| Audience | What to emphasise |
|---|---|
| **HR** | "I built an automated tool that turns raw stock data into clear reports. It handles data fetching, cleaning, analysis, and presentation — the full analyst workflow. It shows I can take a business question and deliver a working product." |
| **Technical** | "The architecture is modular: `data_loader.py` handles ingestion with a fallback chain, `analyzer.py` computes financial metrics using pandas & numpy, `visualization.py` renders charts with matplotlib/seaborn, and `report.py` generates plain-English summaries. It's CLI-driven with argparse and includes a Streamlit dashboard for interactivity. I tested with both synthetic data (GBM) and real Yahoo Finance data." |

---

## 🧠 Key Concepts to Memorise

| Term | Definition |
|---|---|
| **OHLCV** | Open, High, Low, Close, Volume |
| **Daily Return** | pct_change() of close prices |
| **SMA** | Simple moving average |
| **Volatility** | Std dev of returns, annualised × √252 |
| **Sharpe Ratio** | (Return - Rf) / Volatility |
| **Max Drawdown** | Peak-to-trough decline |
| **Support** | Price level where buying tends to kick in |
| **Resistance** | Price level where selling tends to kick in |
| **Golden Cross** | 50-day SMA crosses above 200-day SMA |
| **Death Cross** | 50-day SMA crosses below 200-day SMA |

---

*Remember: This project is for EDUCATIONAL PURPOSES. It is NOT financial advice.*
