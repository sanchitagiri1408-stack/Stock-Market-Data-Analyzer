# ▶️ How to Run the Project

---

## Quick start (3 commands)

```bash
# 1. Open terminal in the project folder
# 2. Activate virtual environment (if not already)
#    Windows: venv\Scripts\activate
#    Mac/Linux: source venv/bin/activate

# 3. Run the analyzer
python main.py
```

That's it. Watch the terminal, then open `outputs/` for charts and reports.

---

## Command-line options

```bash
python main.py --help
```

| Option | Default | Description |
|---|---|---|
| `--ticker` | AAPL | Stock symbol (e.g., MSFT, GOOGL, RELIANCE.NS) |
| `--start` | 2023-01-01 | Start date (YYYY-MM-DD) |
| `--end` | 2024-12-31 | End date (YYYY-MM-DD) |
| `--csv` | None | Path to local CSV file |
| `--outdir` | outputs | Output directory |
| `--dashboard` | flag | Launch Streamlit dashboard |

---

## Examples

### Analyse Apple for 2023

```bash
python main.py --ticker AAPL --start 2023-01-01 --end 2023-12-31
```

### Analyse Microsoft using a local CSV

```bash
python main.py --ticker MSFT --csv data/sample_aapl.csv
```

### Launch the interactive dashboard

```bash
streamlit run dashboard.py
```

Then open <http://localhost:8501> in your browser.

---

## Expected terminal output

```
=================================================================
  STOCK MARKET DATA ANALYZER
=================================================================
  Ticker : AAPL
  Range  : 2023-01-01 to 2024-12-31
  Output : outputs/
=================================================================

[Step 1/5] Loading stock data...
  -> 522 rows loaded

[Step 2/5] Cleaning data...
  -> Removed 0 rows (duplicates / missing values)
  -> Clean dataset: 522 rows

[Step 3/5] Running analysis...
  -> Computed: daily returns, cumulative returns, SMAs, volatility

[Step 4/5] Generating charts...
  -> Generated 9 charts

[Step 5/5] Generating report...
  -> Saved report -> outputs/AAPL_analysis_report.txt
  -> Saved markdown report -> outputs/AAPL_analysis_report.md
  -> Saved processed data   -> outputs/AAPL_processed_data.csv

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

  DONE! Check the outputs/ folder for charts and reports.
  DISCLAIMER: This analysis is for educational purposes only.
  It is NOT financial advice.
```

---

## Generated files

After running, you will find:

| File | Description |
|---|---|
| `outputs/charts/AAPL_price_moving_avg.png` | Price + SMA 20/50/200 |
| `outputs/charts/AAPL_returns_distribution.png` | Histogram of daily returns |
| `outputs/charts/AAPL_cumulative_returns.png` | Cumulative return % |
| `outputs/charts/AAPL_volatility.png` | Rolling 20-day volatility |
| `outputs/charts/AAPL_volume.png` | Trading volume bars |
| `outputs/charts/AAPL_high_low_range.png` | Daily high-low range |
| `outputs/charts/AAPL_monthly_returns_heatmap.png` | Monthly return heatmap |
| `outputs/charts/AAPL_drawdown.png` | Drawdown over time |
| `outputs/charts/AAPL_return_vs_volume.png` | Return vs volume scatter |
| `outputs/AAPL_analysis_report.txt` | Human-readable report |
| `outputs/AAPL_analysis_report.md` | Markdown report |
| `outputs/AAPL_processed_data.csv` | Enriched dataset |

---

## Common errors & fixes

| Error | Fix |
|---|---|
| `ModuleNotFoundError: yfinance` | `pip install yfinance` |
| `No data returned for ticker` | Check ticker symbol spelling |
| `Permission denied` | `chmod +x main.py` (Mac/Linux) |
| `streamlit: command not found` | `pip install streamlit` |

---

*Educational project. Not financial advice.*
