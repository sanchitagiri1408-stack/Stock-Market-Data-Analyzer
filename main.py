"""
=============================================================================
 Stock Market Data Analyzer
=============================================================================
 A beginner-friendly, modular Python project that:
   1. Fetches stock data from Yahoo Finance (or falls back to CSV / synthetic)
   2. Cleans and prepares the data
   3. Computes daily returns, moving averages, volatility, risk metrics
   4. Generates professional charts
   5. Produces a text + markdown analysis report

 Usage:
   python main.py                     # default: AAPL, 2023-01-01 to 2024-12-31
   python main.py --ticker MSFT       # custom ticker
   python main.py --csv data.csv      # use a local CSV file
   python main.py --start 2022-01-01 --end 2023-01-01
   python main.py --dashboard         # launch Streamlit dashboard

 Disclaimer: This project is for EDUCATIONAL PURPOSES ONLY.
 It is NOT financial advice. Do not use it to make investment decisions.
=============================================================================
"""

import argparse
import os
import sys

# Ensure src/ is on the Python path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from data_loader import load_data
from analyzer import run_full_analysis, compute_summary
from visualization import generate_all_charts
from report import generate_text_report, generate_markdown_report, save_report


# ---------------------------------------------------------------------------
# Default configuration
# ---------------------------------------------------------------------------
DEFAULT_TICKER = "AAPL"
DEFAULT_START = "2023-01-01"
DEFAULT_END = "2024-12-31"
MA_WINDOWS = [20, 50, 200]
VOL_WINDOW = 20


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Stock Market Data Analyzer - analyse stock data with Python"
    )
    parser.add_argument("--ticker", type=str, default=DEFAULT_TICKER,
                        help="Stock ticker symbol (default: AAPL)")
    parser.add_argument("--start", type=str, default=DEFAULT_START,
                        help="Start date YYYY-MM-DD (default: 2023-01-01)")
    parser.add_argument("--end", type=str, default=DEFAULT_END,
                        help="End date YYYY-MM-DD (default: 2024-12-31)")
    parser.add_argument("--csv", type=str, default=None,
                        help="Path to a local CSV file (fallback)")
    parser.add_argument("--outdir", type=str, default="outputs",
                        help="Output directory for charts and reports")
    parser.add_argument("--dashboard", action="store_true",
                        help="Launch the Streamlit dashboard instead")
    return parser.parse_args()


def run_pipeline(ticker, start, end, csv_path, outdir):
    """
    Execute the full analysis pipeline:
    load -> clean -> analyse -> visualise -> report.
    """
    print("\n" + "=" * 65)
    print("  STOCK MARKET DATA ANALYZER")
    print("=" * 65)
    print(f"  Ticker : {ticker}")
    print(f"  Range  : {start} to {end}")
    print(f"  Output : {outdir}/")
    print("=" * 65 + "\n")

    # ---- Step 1: Load data ------------------------------------------------
    print("[Step 1/5] Loading stock data...")
    df = load_data(ticker=ticker, start=start, end=end, csv_path=csv_path)
    print(f"  -> {len(df)} rows loaded\n")

    # ---- Step 2: Clean data -----------------------------------------------
    print("[Step 2/5] Cleaning data...")
    # Remove rows with missing critical values
    before = len(df)
    df = df.dropna(subset=["Open", "High", "Low", "Close", "Volume"])
    # Remove duplicate dates
    df = df.drop_duplicates(subset=["Date"], keep="last")
    # Sort by date ascending
    df = df.sort_values("Date").reset_index(drop=True)
    after = len(df)
    removed = before - after
    print(f"  -> Removed {removed} rows (duplicates / missing values)")
    print(f"  -> Clean dataset: {after} rows\n")

    # ---- Step 3: Analyse --------------------------------------------------
    print("[Step 3/5] Running analysis...")
    df = run_full_analysis(df, ma_windows=MA_WINDOWS, vol_window=VOL_WINDOW)
    print("  -> Computed: daily returns, cumulative returns, SMAs, volatility\n")

    # ---- Step 4: Visualise ------------------------------------------------
    print("[Step 4/5] Generating charts...")
    chart_dir = os.path.join(outdir, "charts")
    os.makedirs(chart_dir, exist_ok=True)
    chart_paths = generate_all_charts(df, ticker, chart_dir)
    print(f"  -> Generated {len(chart_paths)} charts\n")

    # ---- Step 5: Report ---------------------------------------------------
    print("[Step 5/5] Generating report...")
    summary = compute_summary(df, ticker=ticker)

    report_text = generate_text_report(summary, chart_paths)
    report_path = save_report(report_text, outdir, ticker)

    md_text = generate_markdown_report(summary, chart_paths)
    md_path = os.path.join(outdir, f"{ticker}_analysis_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"  -> Saved markdown report -> {md_path}")

    # Also save processed data to CSV for reference
    processed_path = os.path.join(outdir, f"{ticker}_processed_data.csv")
    df.to_csv(processed_path, index=False)
    print(f"  -> Saved processed data   -> {processed_path}")

    # ---- Summary to console -----------------------------------------------
    print("\n" + "=" * 65)
    print("  ANALYSIS SUMMARY")
    print("=" * 65)
    for key, value in summary.items():
        print(f"  {key:.<30} {value}")
    print("=" * 65)
    print("\n  DONE! Check the outputs/ folder for charts and reports.")
    print("  DISCLAIMER: This analysis is for educational purposes only.")
    print("  It is NOT financial advice.\n")

    return df, summary, chart_paths, report_path


def main():
    args = parse_args()

    if args.dashboard:
        # Optional: launch Streamlit dashboard
        try:
            import streamlit
        except ImportError:
            print("Streamlit not installed. Run: pip install streamlit")
            sys.exit(1)
        dashboard_path = os.path.join(os.path.dirname(__file__), "dashboard.py")
        os.system(f"streamlit run {dashboard_path}")
        return

    run_pipeline(
        ticker=args.ticker,
        start=args.start,
        end=args.end,
        csv_path=args.csv,
        outdir=args.outdir,
    )


if __name__ == "__main__":
    main()
