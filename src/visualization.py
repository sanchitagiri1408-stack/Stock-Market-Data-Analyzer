"""
visualization.py
================
All chart-producing functions. Each function saves a PNG to the outputs
directory and returns the file path.
"""

import os
import matplotlib
matplotlib.use("Agg")  # non-interactive backend - safe for servers
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd
import numpy as np

# Global style
sns.set_style("whitegrid")
plt.rcParams.update({
    "figure.figsize": (14, 6),
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
})

PALETTE = {
    "price": "#1f77b4",
    "sma20": "#ff7f0e",
    "sma50": "#2ca02c",
    "sma200": "#d62728",
    "returns": "#9467bd",
    "volatility": "#8c564b",
    "accent": "#17becf",
}


def _save(fig, path: str) -> str:
    """Save figure, close it, return path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [viz] Saved chart -> {path}")
    return path


# ---------------------------------------------------------------------------
# 1. Closing price with moving averages
# ---------------------------------------------------------------------------

def plot_price_with_moving_averages(df: pd.DataFrame, ticker: str, outdir: str) -> str:
    fig, ax = plt.subplots()

    ax.plot(df["Date"], df["Close"], label="Close Price",
            color=PALETTE["price"], linewidth=1.2)

    for col, color in [("SMA_20", PALETTE["sma20"]),
                        ("SMA_50", PALETTE["sma50"]),
                        ("SMA_200", PALETTE["sma200"])]:
        if col in df.columns:
            ax.plot(df["Date"], df[col], label=col.replace("_", " "),
                    color=color, linewidth=1.0, alpha=0.85)

    ax.set_title(f"{ticker} - Closing Price & Moving Averages")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend(loc="best")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate()

    return _save(fig, os.path.join(outdir, f"{ticker}_price_moving_avg.png"))


# ---------------------------------------------------------------------------
# 2. Daily returns histogram + KDE
# ---------------------------------------------------------------------------

def plot_daily_returns_distribution(df: pd.DataFrame, ticker: str, outdir: str) -> str:
    returns = df["Daily_Return"].dropna()

    fig, ax = plt.subplots()
    sns.histplot(returns, bins=60, kde=True, color=PALETTE["returns"], ax=ax)

    mean_r = returns.mean()
    std_r = returns.std()
    ax.axvline(mean_r, color="red", linestyle="--", linewidth=1.5,
               label=f"Mean = {mean_r:.4f}")
    ax.axvline(mean_r + 2 * std_r, color="orange", linestyle=":", linewidth=1.2,
               label=f"+2σ = {mean_r + 2*std_r:.4f}")
    ax.axvline(mean_r - 2 * std_r, color="orange", linestyle=":", linewidth=1.2,
               label=f"-2σ = {mean_r - 2*std_r:.4f}")

    ax.set_title(f"{ticker} - Daily Returns Distribution")
    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")
    ax.legend()

    return _save(fig, os.path.join(outdir, f"{ticker}_returns_distribution.png"))


# ---------------------------------------------------------------------------
# 3. Cumulative returns
# ---------------------------------------------------------------------------

def plot_cumulative_returns(df: pd.DataFrame, ticker: str, outdir: str) -> str:
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Cumulative_Return"] * 100,
            color=PALETTE["accent"], linewidth=1.4)
    ax.fill_between(df["Date"], df["Cumulative_Return"] * 100, 0,
                    where=(df["Cumulative_Return"] >= 0),
                    color=PALETTE["accent"], alpha=0.15)
    ax.axhline(0, color="grey", linewidth=0.8)

    ax.set_title(f"{ticker} - Cumulative Returns (%)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Return (%)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate()

    return _save(fig, os.path.join(outdir, f"{ticker}_cumulative_returns.png"))


# ---------------------------------------------------------------------------
# 4. Volatility over time
# ---------------------------------------------------------------------------

def plot_volatility(df: pd.DataFrame, ticker: str, outdir: str) -> str:
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Volatility"] * 100,
            color=PALETTE["volatility"], linewidth=1.0)
    ax.set_title(f"{ticker} - Rolling Volatility (20-day window, %)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility (%)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate()

    return _save(fig, os.path.join(outdir, f"{ticker}_volatility.png"))


# ---------------------------------------------------------------------------
# 5. Volume bar chart
# ---------------------------------------------------------------------------

def plot_volume(df: pd.DataFrame, ticker: str, outdir: str) -> str:
    fig, ax = plt.subplots()
    colors = ["green" if df["Close"].iloc[i] >= df["Open"].iloc[i] else "red"
              for i in range(len(df))]
    ax.bar(df["Date"], df["Volume"] / 1e6, color=colors, alpha=0.7, width=1.5)
    ax.set_title(f"{ticker} - Trading Volume (millions)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Volume (M)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate()

    return _save(fig, os.path.join(outdir, f"{ticker}_volume.png"))


# ---------------------------------------------------------------------------
# 6. High-Low price range with close
# ---------------------------------------------------------------------------

def plot_high_low_range(df: pd.DataFrame, ticker: str, outdir: str) -> str:
    fig, ax = plt.subplots()
    ax.fill_between(df["Date"], df["Low"], df["High"],
                    color=PALETTE["price"], alpha=0.15, label="High-Low Range")
    ax.plot(df["Date"], df["Close"], color=PALETTE["price"], linewidth=0.8,
            label="Close")
    ax.set_title(f"{ticker} - Daily High/Low Range with Close")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price ($)")
    ax.legend()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate()

    return _save(fig, os.path.join(outdir, f"{ticker}_high_low_range.png"))


# ---------------------------------------------------------------------------
# 7. Monthly returns heatmap
# ---------------------------------------------------------------------------

def plot_monthly_returns_heatmap(df: pd.DataFrame, ticker: str, outdir: str) -> str:
    df_copy = df.copy()
    df_copy["Year"] = df_copy["Date"].dt.year
    df_copy["Month"] = df_copy["Date"].dt.month

    monthly = df_copy.groupby(["Year", "Month"])["Daily_Return"].apply(
        lambda x: (1 + x).prod() - 1
    ).unstack()

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.heatmap(monthly * 100, annot=True, fmt=".1f", cmap="RdYlGn",
                center=0, ax=ax, cbar_kws={"label": "Return (%)"})
    ax.set_title(f"{ticker} - Monthly Returns Heatmap (%)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Year")

    return _save(fig, os.path.join(outdir, f"{ticker}_monthly_returns_heatmap.png"))


# ---------------------------------------------------------------------------
# 8. Drawdown chart
# ---------------------------------------------------------------------------

def plot_drawdown(df: pd.DataFrame, ticker: str, outdir: str) -> str:
    prices = df["Close"]
    rolling_max = prices.cummax()
    drawdown = prices / rolling_max - 1

    fig, ax = plt.subplots()
    ax.fill_between(df["Date"], drawdown * 100, 0,
                    color="red", alpha=0.3, label="Drawdown")
    ax.plot(df["Date"], drawdown * 100, color="darkred", linewidth=0.8)
    ax.set_title(f"{ticker} - Drawdown Over Time (%)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Drawdown (%)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.autofmt_xdate()

    return _save(fig, os.path.join(outdir, f"{ticker}_drawdown.png"))


# ---------------------------------------------------------------------------
# 9. Scatter: daily return vs volume
# ---------------------------------------------------------------------------

def plot_return_vs_volume(df: pd.DataFrame, ticker: str, outdir: str) -> str:
    fig, ax = plt.subplots()
    ax.scatter(df["Volume"] / 1e6, df["Daily_Return"] * 100,
               alpha=0.4, s=10, color=PALETTE["returns"])
    ax.set_title(f"{ticker} - Daily Return vs Trading Volume")
    ax.set_xlabel("Volume (millions)")
    ax.set_ylabel("Daily Return (%)")

    return _save(fig, os.path.join(outdir, f"{ticker}_return_vs_volume.png"))


# ---------------------------------------------------------------------------
# Master function: generate all charts
# ---------------------------------------------------------------------------

def generate_all_charts(df: pd.DataFrame, ticker: str, outdir: str) -> list:
    """Run every chart function and return list of saved file paths."""
    paths = []
    paths.append(plot_price_with_moving_averages(df, ticker, outdir))
    paths.append(plot_daily_returns_distribution(df, ticker, outdir))
    paths.append(plot_cumulative_returns(df, ticker, outdir))
    paths.append(plot_volatility(df, ticker, outdir))
    paths.append(plot_volume(df, ticker, outdir))
    paths.append(plot_high_low_range(df, ticker, outdir))
    paths.append(plot_monthly_returns_heatmap(df, ticker, outdir))
    paths.append(plot_drawdown(df, ticker, outdir))
    paths.append(plot_return_vs_volume(df, ticker, outdir))
    return paths
