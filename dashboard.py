"""
dashboard.py
============
Optional Streamlit dashboard for the Stock Market Data Analyzer.

Run with:
    streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from data_loader import load_data
from analyzer import run_full_analysis, compute_summary
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Market Data Analyzer", layout="wide")

st.title("📈 Stock Market Data Analyzer")
st.markdown("*"
    "Interactive dashboard for stock price analysis. "
    "For educational purposes only - NOT financial advice."
)

# --- Sidebar controls ---
st.sidebar.header("Configuration")
ticker = st.sidebar.text_input("Ticker Symbol", value="AAPL")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))
csv_path = st.sidebar.text_input("CSV Path (optional)", value="")

if st.sidebar.button("Analyze"):
    with st.spinner("Loading data..."):
        df = load_data(
            ticker=ticker,
            start=start_date.strftime("%Y-%m-%d"),
            end=end_date.strftime("%Y-%m-%d"),
            csv_path=csv_path if csv_path else None,
        )

    with st.spinner("Analysing..."):
        df = run_full_analysis(df)
        summary = compute_summary(df, ticker=ticker)

    st.subheader(f"Analysis Results: {ticker}")

    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Start Price", f"${summary['Start Price']:.2f}")
    col2.metric("End Price", f"${summary['End Price']:.2f}")
    col3.metric("Total Return", f"{summary['Total Return (%)']:.2f}%")
    col4.metric("Sharpe Ratio", f"{summary['Sharpe Ratio (rf=0%)']:.2f}")

    # Charts
    st.subheader("Price & Moving Averages")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(df["Date"], df["Close"], label="Close")
    for col in ["SMA_20", "SMA_50", "SMA_200"]:
        if col in df.columns:
            ax1.plot(df["Date"], df[col], label=col)
    ax1.legend()
    ax1.set_title("Price with Moving Averages")
    st.pyplot(fig1)

    st.subheader("Daily Returns Distribution")
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.hist(df["Daily_Return"].dropna(), bins=60, color="purple", alpha=0.7)
    ax2.set_title("Daily Returns")
    st.pyplot(fig2)

    st.subheader("Full Summary")
    st.write(summary)

    st.download_button(
        label="Download Report (CSV)",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name=f"{ticker}_analysis.csv",
        mime="text/csv",
    )
