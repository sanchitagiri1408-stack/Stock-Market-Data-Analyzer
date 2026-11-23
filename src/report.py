"""
report.py
=========
Generates a human-readable analysis report (text + markdown).
"""

import os
from datetime import datetime


def generate_text_report(summary: dict, chart_paths: list = None) -> str:
    """
    Build a plain-text report string from the summary dictionary.
    """
    lines = []
    lines.append("=" * 65)
    lines.append("   STOCK MARKET DATA ANALYZER - ANALYSIS REPORT")
    lines.append("=" * 65)
    lines.append(f"   Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 65)
    lines.append("")

    # --- Overview ---
    lines.append("1. OVERVIEW")
    lines.append("-" * 40)
    lines.append(f"   Ticker          : {summary['Ticker']}")
    lines.append(f"   Date Range      : {summary['Date Range']}")
    lines.append(f"   Trading Days    : {summary['Trading Days']}")
    lines.append("")

    # --- Price summary ---
    lines.append("2. PRICE SUMMARY")
    lines.append("-" * 40)
    lines.append(f"   Start Price     : ${summary['Start Price']:.2f}")
    lines.append(f"   End Price       : ${summary['End Price']:.2f}")
    lines.append(f"   Highest Price   : ${summary['Highest Price']:.2f}")
    lines.append(f"   Lowest Price    : ${summary['Lowest Price']:.2f}")
    lines.append(f"   Average Price   : ${summary['Average Price']:.2f}")
    lines.append(f"   Total Return    : {summary['Total Return (%)']:.2f}%")
    lines.append("")

    # --- Risk & return ---
    lines.append("3. RISK & RETURN METRICS")
    lines.append("-" * 40)
    lines.append(f"   Avg Daily Return      : {summary['Average Daily Return (%)']:.4f}%")
    lines.append(f"   Daily Std Dev         : {summary['Daily Return Std Dev (%)']:.4f}%")
    lines.append(f"   Annualised Return     : {summary['Annualised Return (%)']:.2f}%")
    lines.append(f"   Annualised Volatility : {summary['Annualised Volatility (%)']:.2f}%")
    lines.append(f"   Sharpe Ratio          : {summary['Sharpe Ratio (rf=0%)']:.4f}")
    lines.append(f"   Max Drawdown          : {summary['Max Drawdown (%)']:.2f}%")
    lines.append("")

    # --- Technical levels ---
    lines.append("4. TECHNICAL LEVELS")
    lines.append("-" * 40)
    lines.append(f"   Support (25th pct)    : ${summary['Support (25th pct)']:.2f}")
    lines.append(f"   Resistance (75th pct) : ${summary['Resistance (75th pct)']:.2f}")
    lines.append(f"   Trend (SMA 50/200)    : {summary['Trend (SMA 50 vs 200)']}")
    lines.append("")

    # --- Interpretation ---
    lines.append("5. INTERPRETATION")
    lines.append("-" * 40)
    lines.append(interpret_summary(summary))
    lines.append("")

    # --- Charts ---
    if chart_paths:
        lines.append("6. GENERATED CHARTS")
        lines.append("-" * 40)
        for p in chart_paths:
            lines.append(f"   - {os.path.basename(p)}")
        lines.append("")

    lines.append("=" * 65)
    lines.append("   DISCLAIMER: This report is for educational purposes only.")
    lines.append("   It is NOT financial advice. Always do your own research.")
    lines.append("=" * 65)

    return "\n".join(lines)


def interpret_summary(summary: dict) -> str:
    """
    Produce plain-English interpretation of the summary metrics.
    """
    parts = []

    total_ret = summary["Total Return (%)"]
    if total_ret > 20:
        parts.append(f"The stock gained {total_ret:.1f}% over the period - a strong performance.")
    elif total_ret > 0:
        parts.append(f"The stock rose {total_ret:.1f}% over the period - a positive but modest gain.")
    elif total_ret > -20:
        parts.append(f"The stock fell {abs(total_ret):.1f}% over the period - a moderate decline.")
    else:
        parts.append(f"The stock dropped {abs(total_ret):.1f}% over the period - a significant decline.")

    vol = summary["Annualised Volatility (%)"]
    if vol > 40:
        parts.append(f"Annualised volatility of {vol:.1f}% indicates HIGH risk.")
    elif vol > 20:
        parts.append(f"Annualised volatility of {vol:.1f}% indicates MODERATE-to-HIGH risk.")
    else:
        parts.append(f"Annualised volatility of {vol:.1f}% indicates relatively LOW risk.")

    sharpe = summary["Sharpe Ratio (rf=0%)"]
    if sharpe > 1.5:
        parts.append(f"Sharpe ratio of {sharpe:.2f} suggests excellent risk-adjusted returns.")
    elif sharpe > 0.5:
        parts.append(f"Sharpe ratio of {sharpe:.2f} suggests acceptable risk-adjusted returns.")
    else:
        parts.append(f"Sharpe ratio of {sharpe:.2f} suggests poor risk-adjusted returns.")

    dd = summary["Max Drawdown (%)"]
    parts.append(f"Maximum drawdown of {abs(dd):.1f}% shows the worst peak-to-trough loss.")

    trend = summary["Trend (SMA 50 vs 200)"]
    parts.append(f"Current trend signal: {trend}.")

    return "\n   ".join(parts)


def save_report(report_text: str, outdir: str, ticker: str) -> str:
    """Save report to a .txt file and return the path."""
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, f"{ticker}_analysis_report.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"  [report] Saved report -> {path}")
    return path


def generate_markdown_report(summary: dict, chart_paths: list = None) -> str:
    """
    Build a Markdown report string (useful for GitHub README or docs).
    """
    md = []
    md.append(f"# Stock Analysis Report - {summary['Ticker']}")
    md.append(f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    md.append("")
    md.append("## Price Summary")
    md.append(f"| Metric | Value |")
    md.append(f"|---|---|")
    md.append(f"| Date Range | {summary['Date Range']} |")
    md.append(f"| Trading Days | {summary['Trading Days']} |")
    md.append(f"| Start Price | ${summary['Start Price']:.2f} |")
    md.append(f"| End Price | ${summary['End Price']:.2f} |")
    md.append(f"| Highest Price | ${summary['Highest Price']:.2f} |")
    md.append(f"| Lowest Price | ${summary['Lowest Price']:.2f} |")
    md.append(f"| Total Return | {summary['Total Return (%)']:.2f}% |")
    md.append("")
    md.append("## Risk & Return")
    md.append(f"| Metric | Value |")
    md.append(f"|---|---|")
    md.append(f"| Avg Daily Return | {summary['Average Daily Return (%)']:.4f}% |")
    md.append(f"| Daily Std Dev | {summary['Daily Return Std Dev (%)']:.4f}% |")
    md.append(f"| Annualised Return | {summary['Annualised Return (%)']:.2f}% |")
    md.append(f"| Annualised Volatility | {summary['Annualised Volatility (%)']:.2f}% |")
    md.append(f"| Sharpe Ratio | {summary['Sharpe Ratio (rf=0%)']:.4f} |")
    md.append(f"| Max Drawdown | {summary['Max Drawdown (%)']:.2f}% |")
    md.append("")
    md.append("## Technical Levels")
    md.append(f"| Metric | Value |")
    md.append(f"|---|---|")
    md.append(f"| Support | ${summary['Support (25th pct)']:.2f} |")
    md.append(f"| Resistance | ${summary['Resistance (75th pct)']:.2f} |")
    md.append(f"| Trend | {summary['Trend (SMA 50 vs 200)']} |")
    md.append("")
    md.append("## Interpretation")
    md.append(interpret_summary(summary))
    md.append("")

    if chart_paths:
        md.append("## Charts")
        for p in chart_paths:
            name = os.path.basename(p)
            md.append(f"![{name}](../outputs/charts/{name})")
            md.append("")

    md.append("---")
    md.append("*Disclaimer: This report is for educational purposes only and is not financial advice.*")
    return "\n".join(md)
