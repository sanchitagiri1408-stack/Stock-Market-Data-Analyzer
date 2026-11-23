"""
data_loader.py
==============
Handles loading stock data from either:
1. Yahoo Finance (via yfinance) - primary source
2. Local CSV file - fallback source
3. Synthetic data generator - for demo/testing when no internet
"""

import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def fetch_from_yfinance(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Fetch stock data from Yahoo Finance using yfinance.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol, e.g. "AAPL" or "RELIANCE.NS"
    start : str
        Start date in "YYYY-MM-DD" format
    end : str
        End date in "YYYY-MM-DD" format

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: Date, Open, High, Low, Close, Adj Close, Volume
    """
    try:
        import yfinance as yf
    except ImportError:
        raise ImportError(
            "yfinance is not installed. Run: pip install yfinance"
        )

    print(f"  [data_loader] Fetching {ticker} from Yahoo Finance...")
    df = yf.download(ticker, start=start, end=end, auto_adjust=False)

    if df.empty:
        raise ValueError(f"No data returned for ticker '{ticker}'")

    # Flatten multi-level columns if present (yfinance >= 0.2.51)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Reset index so Date becomes a column
    df = df.reset_index()
    df = df.rename(columns={"Date": "Date"})

    print(f"  [data_loader] Fetched {len(df)} rows from Yahoo Finance")
    return df


def load_from_csv(filepath: str) -> pd.DataFrame:
    """
    Load stock data from a local CSV file.

    Expected columns: Date, Open, High, Low, Close, Adj Close, Volume
    (case-insensitive; extra columns are kept but ignored).

    Parameters
    ----------
    filepath : str
        Path to the CSV file

    Returns
    -------
    pd.DataFrame
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")

    print(f"  [data_loader] Loading CSV: {filepath}")
    df = pd.read_csv(filepath)

    # Normalize column names (strip whitespace, title-case)
    df.columns = [c.strip().title() for c in df.columns]

    required = {"Date", "Open", "High", "Low", "Close", "Volume"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CSV missing required columns: {missing}")

    print(f"  [data_loader] Loaded {len(df)} rows from CSV")
    return df


def generate_sample_data(
    ticker: str = "AAPL",
    start: str = "2023-01-01",
    end: str = "2024-12-31",
    initial_price: float = 150.0,
    drift: float = 0.0003,
    volatility: float = 0.015,
) -> pd.DataFrame:
    """
    Generate synthetic stock data using Geometric Brownian Motion (GBM).

    This simulates realistic-looking price movement for demo purposes.

    Parameters
    ----------
    ticker : str
        Ticker symbol to label the data
    start : str
        Start date "YYYY-MM-DD"
    end : str
        End date "YYYY-MM-DD"
    initial_price : float
        Starting price
    drift : float
        Daily drift (average return)
    volatility : float
        Daily volatility (std dev of returns)

    Returns
    -------
    pd.DataFrame
        Synthetic OHLCV data
    """
    print(f"  [data_loader] Generating sample data for {ticker}...")

    dates = pd.date_range(start=start, end=end, freq="B")  # business days only
    n = len(dates)

    # Daily returns from normal distribution
    daily_returns = np.random.normal(drift, volatility, n)

    # Build price path via cumulative product (GBM)
    price_path = initial_price * np.exp(np.cumsum(daily_returns))

    # Derive OHLC from close with small random perturbations
    open_prices = price_path * (1 + np.random.normal(0, 0.003, n))
    high_prices = np.maximum(open_prices, price_path) * (1 + np.abs(np.random.normal(0, 0.005, n)))
    low_prices = np.minimum(open_prices, price_path) * (1 - np.abs(np.random.normal(0, 0.005, n)))
    volume = np.random.randint(50_000_000, 150_000_000, n)

    df = pd.DataFrame({
        "Date": dates,
        "Open": np.round(open_prices, 2),
        "High": np.round(high_prices, 2),
        "Low": np.round(low_prices, 2),
        "Close": np.round(price_path, 2),
        "Adj Close": np.round(price_path, 2),
        "Volume": volume,
    })

    print(f"  [data_loader] Generated {len(df)} rows of sample data")
    return df


def load_data(
    ticker: str = "AAPL",
    start: str = "2023-01-01",
    end: str = "2024-12-31",
    csv_path: str = None,
) -> pd.DataFrame:
    """
    Load stock data with automatic fallback:
    1. Try yfinance if available and internet works
    2. Fall back to CSV if provided
    3. Fall back to synthetic sample data

    Parameters
    ----------
    ticker : str
        Stock ticker symbol
    start : str
        Start date "YYYY-MM-DD"
    end : str
        End date "YYYY-MM-DD"
    csv_path : str, optional
        Path to a CSV file as fallback

    Returns
    -------
    pd.DataFrame
        Stock data with Date column as datetime
    """
    df = None

    # 1. Try yfinance
    try:
        df = fetch_from_yfinance(ticker, start, end)
    except Exception as e:
        print(f"  [data_loader] yfinance failed: {e}")

    # 2. Try CSV fallback
    if df is None and csv_path and os.path.exists(csv_path):
        try:
            df = load_from_csv(csv_path)
        except Exception as e:
            print(f"  [data_loader] CSV fallback failed: {e}")

    # 3. Generate synthetic sample data
    if df is None:
        print("  [data_loader] No external data source available; using synthetic sample data")
        df = generate_sample_data(ticker, start, end)

    # Ensure Date column is datetime
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    return df
