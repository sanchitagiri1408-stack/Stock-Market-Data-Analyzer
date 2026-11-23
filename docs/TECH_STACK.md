# 🛠️ Tech Stack Options

Three options are presented below, from easiest to most advanced.

---

## Option A — Easy (Recommended for Students)

| Component | Tool |
|---|---|
| Language | Python 3.10+ |
| Data | pandas, numpy |
| Viz | matplotlib, seaborn |
| Data source | yfinance (or CSV) |
| Output | Text report + PNG charts |

**Difficulty:** ⭐ Beginner

**Expected output:**
- Console summary of metrics
- 9 chart PNGs
- Text + Markdown report

**Why choose this:** Minimal setup, no web framework, no database. Perfect for
a course project. You learn pandas, financial math, and visualisation.

---

## Option B — Intermediate

| Component | Tool |
|---|---|
| Language | Python 3.10+ |
| Data | pandas, numpy |
| Viz | matplotlib, seaborn, **plotly** |
| Data source | yfinance + **Alpha Vantage API** |
| Dashboard | **Streamlit** |
| Output | Interactive charts + web dashboard |

**Difficulty:** ⭐⭐ Intermediate

**Expected output:**
- Everything in Option A
- Interactive Plotly charts (zoom, hover, pan)
- Streamlit web app with sidebar controls

**Why choose this:** Adds interactivity and a web UI. Great for portfolio
pieces and demoing to non-technical reviewers.

---

## Option C — Advanced

| Component | Tool |
|---|---|
| Language | Python 3.10+ |
| Data | pandas, numpy, **SQLAlchemy** |
| Viz | plotly, **dash** |
| Data source | yfinance + **Polygon.io / Tiingo API** |
| Storage | **PostgreSQL / SQLite** |
| Dashboard | **Dash** or **Streamlit Cloud** |
| Testing | **pytest** |
| CI/CD | **GitHub Actions** |
| Deployment | **Docker** |

**Difficulty:** ⭐⭐⭐ Advanced

**Expected output:**
- Everything in Option B
- Database-backed storage
- Automated tests
- CI pipeline
- Docker container
- Deployed dashboard

**Why choose this:** Industry-grade. Best for capstone projects or job
applications targeting senior roles.

---

## ✅ Recommendation for Students

**Choose Option A.** It covers 90% of what interviewers look for:
- Clean modular code
- Real financial calculations
- Professional charts
- Working CLI
- Good README

You can always add Option B/C features later as stretch goals.

---

*Educational project. Not financial advice.*
