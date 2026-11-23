"""
analyzer.py
===========
Core financial analysis module.

Computes:
- Daily returns
- Cumulative returns
- Moving averages (SMA)
- Volatility (rolling std dev of returns)
- Sharpe ratio
- Max drawdown
- Trend identification
- Support / resistance levels
"""

import pandas as pd
import numpy as np


# ---------------------------------------------------------------------------
# Returns
# ---------------------------------------------------------------------------

def compute_daily_returns(df: pd.DataFrame, price_col: str = "Close") -> pd.DataFrame:
    """
    Add a 'Daily_Return' column = percentage change of price_col.

    Formula: (P_t / P_{t-1}) - 1
    """
    df = df.copy()
    df["Daily_Return"] = df[price_col].pct_change()
    return df


def compute_cumulative_returns(df: pd.DataFrame, price_col: str = "Close") -> pd.DataFrame:
    """
    Add a 'Cumulative_Return' column = total return from the first row.

    Formula: (P_t / P_0) - 1
    """
    df = df.copy()
    df["Cumulative_Return"] = df[price_col] / df[price_col].iloc[0] - 1
    return df


# ---------------------------------------------------------------------------
# Moving averages
# ---------------------------------------------------------------------------

def compute_moving_averages(
    df: pd.DataFrame,
    windows: list = None,
    price_col: str = "Close",
) -> pd.DataFrame:
    """
    Add Simple Moving Average columns for each window.

    Example: windows=[20, 50, 200] -> SMA_20, SMA_50, SMA_200
    """
    if windows is None:
        windows = [20, 50, 200]

    df = df.copy()
    for w in windows:
        col_name = f"SMA_{w}"
        df[col_name] = df[price_col].rolling(window=w, min_periods=1).mean()
    return df


# ---------------------------------------------------------------------------
# Volatility
# ---------------------------------------------------------------------------

def compute_volatility(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    Add a 'Volatility' column = rolling std dev of daily returns.

    Annualised volatility = daily_std * sqrt(252)
    """
    df = df.copy()
    df["Volatility"] = df["Daily_Return"].rolling(window=window, min_periods=1).std()
    return df


# ---------------------------------------------------------------------------
# Risk metrics
# ---------------------------------------------------------------------------

def sharpe_ratio(daily_returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """
    Annualised Sharpe ratio.

    Sharpe = (mean_daily_return - rf_daily) / std_daily_return * sqrt(252)
    """
    returns = daily_returns.dropna()
    if len(returns) == 0 or returns.std() == 0:
        return 0.0
    excess = returns.mean() - risk_free_rate / 252
    return float(excess / returns.std() * np.sqrt(252))


def max_drawdown(prices: pd.Series) -> float:
    """
    Maximum drawdown: largest peak-to-trough decline (%).

    Returns a negative number (e.g. -0.25 = -25% drawdown).
    """
    rolling_max = prices.cummax()
    drawdown = prices / rolling_max - 1
    return float(drawdown.min())


def annualised_return(daily_returns: pd.Series) -> float:
    """Annualised return from daily returns (geometric)."""
    returns = daily_returns.dropna()
    if len(returns) == 0:
        return 0.0
    cumulative = (1 + returns).prod()
    years = len(returns) / 252
    return float(cumulative ** (1 / years) - 1) if years > 0 else 0.0


def annualised_volatility(daily_returns: pd.Series) -> float:
    """Annualised volatility = daily_std * sqrt(252)."""
    returns = daily_returns.dropna()
    if len(returns) == 0:
        return 0.0
    return float(returns.std() * np.sqrt(252))


# ---------------------------------------------------------------------------
# Trend identification
# ---------------------------------------------------------------------------

def identify_trend(df: pd.DataFrame, short_window: int = 50, long_window: int = 200) -> str:
    """
    Simple trend rule using SMA crossover:
      - SMA_short > SMA_long  -> "Uptrend"
      - SMA_short < SMA_long  -> "Downtrend"
      - otherwise             -> "Sideways / Neutral"
    """
    short_col = f"SMA_{short_window}"
    long_col = f"SMA_{long_window}"
    if short_col not in df.columns or long_col not in df.columns:
        return "Unknown"

    latest_short = df[short_col].iloc[-1]
    latest_long = df[long_col].iloc[-1]

    if latest_short > latest_long:
        return "Uptrend"
    elif latest_short < latest_long:
        return "Downtrend"
    else:
        return "Sideways / Neutral"


# ---------------------------------------------------------------------------
# Support / resistance (simple percentile method)
# ---------------------------------------------------------------------------

def support_resistance(df: pd.DataFrame, price_col: str = "Close") -> dict:
    """
    Estimate support and resistance using price percentiles.

    Support  = 25th percentile of closing prices
    Resistance = 75th percentile of closing prices
    """
    prices = df[price_col].dropna()
    if prices.empty:
        return {"support": None, "resistance": None}
    return {
        "support": float(prices.quantile(0.25)),
        "resistance": float(prices.quantile(0.75)),
    }


# ---------------------------------------------------------------------------
# Full analysis pipeline
# ---------------------------------------------------------------------------

def run_full_analysis(
    df: pd.DataFrame,
    ma_windows: list = None,
    vol_window: int = 20,
) -> pd.DataFrame:
    """
    Run all analysis steps on a price DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Raw OHLCV data with 'Date' column.
    ma_windows : list
        Moving-average windows, e.g. [20, 50, 200].
    vol_window : int
        Rolling window for volatility.

    Returns
    -------
    pd.DataFrame
        Enriched DataFrame with Daily_Return, Cumulative_Return,
        SMA_*, Volatility columns.
    """
    if ma_windows is None:
        ma_windows = [20, 50, 200]

    df = compute_daily_returns(df)
    df = compute_cumulative_returns(df)
    df = compute_moving_averages(df, windows=ma_windows)
    df = compute_volatility(df, window=vol_window)

    return df


def compute_summary(df: pd.DataFrame, ticker: str = "STOCK") -> dict:
    """
    Compute a dictionary of summary statistics for the analysed DataFrame.
    """
    returns = df["Daily_Return"].dropna()
    prices = df["Close"]

    sr = support_resistance(df)

    summary = {
        "Ticker": ticker,
        "Date Range": f"{df['Date'].iloc[0].date()} to {df['Date'].iloc[-1].date()}",
        "Trading Days": len(df),
        "Start Price": round(float(prices.iloc[0]), 2),
        "End Price": round(float(prices.iloc[-1]), 2),
        "Highest Price": round(float(prices.max()), 2),
        "Lowest Price": round(float(prices.min()), 2),
        "Average Price": round(float(prices.mean()), 2),
        "Total Return (%)": round(float((prices.iloc[-1] / prices.iloc[0] - 1) * 100), 2),
        "Average Daily Return (%)": round(float(returns.mean() * 100), 4),
        "Daily Return Std Dev (%)": round(float(returns.std() * 100), 4),
        "Annualised Return (%)": round(annualised_return(returns) * 100, 2),
        "Annualised Volatility (%)": round(annualised_volatility(returns) * 100, 2),
        "Sharpe Ratio (rf=0%)": round(sharpe_ratio(returns), 4),
        "Max Drawdown (%)": round(max_drawdown(prices) * 100, 2),
        "Support (25th pct)": round(sr["support"], 2) if sr["support"] else None,
        "Resistance (75th pct)": round(sr["resistance"], 2) if sr["resistance"] else None,
        "Trend (SMA 50 vs 200)": identify_trend(df, 50, 200),
    }
    return summary
