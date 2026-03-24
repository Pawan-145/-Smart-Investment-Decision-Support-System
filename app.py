import yfinance as yf
import pandas as pd
import numpy as np

def fetch_stock_data(tickers, period="1y"):
    data = {}
    for t in tickers:
        try:
            df = yf.Ticker(t).history(period=period)["Close"]
            if len(df) > 0:
                data[t] = df
        except:
            pass
    return data

def calculate_metrics(data):
    metrics = []
    for asset, df in data.items():
        if len(df) < 2:
            continue

        returns = ((df.iloc[-1] - df.iloc[0]) / df.iloc[0]) * 100

        # Annualized volatility
        volatility = np.std(df.pct_change().dropna()) * np.sqrt(252) * 100

        metrics.append({
            "Asset": asset,
            "Return": returns,
            "Risk": volatility
        })

    return pd.DataFrame(metrics)

def portfolio_pie(data):
    num_assets = len(data)
    allocation = {asset: 100/num_assets for asset in data.keys()}
    return pd.DataFrame(list(allocation.items()), columns=["Asset","Allocation"])


# ---------------- Streamlit UI ----------------
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Investment Analyzer", layout="wide")

# 🔥 Dark Theme Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Smart Investment Analyzer")
st.markdown("Compare stocks, analyze risk, and build smarter portfolios 🚀")

# ---------------- Sidebar ----------------
st.sidebar.header("⚙️ Controls")

# Load stock list
df_stocks = pd.read_csv("nse_stock_clean.csv")

assets = st.sidebar.multiselect(
    "Select NSE stocks:",
    options=df_stocks["Symbol"],
    format_func=lambda x: df_stocks.loc[df_stocks["Symbol"] == x, "Company Name"].values[0],
    default=["RELIANCE.NS", "TCS.NS", "INFY.NS"]
)

period = st.sidebar.selectbox(
    "Select Time Period",
    ["1mo", "3mo", "6mo", "1y", "5y"],
    index=3
)

if not assets:
    st.warning("Please select at least one stock!")
    st.stop()

# ---------------- Fetch Data ----------------
with st.spinner("📡 Fetching real-time stock data..."):
    data = fetch_stock_data(assets, period)

if not data:
    st.error("No data found. Try different stocks.")
    st.stop()

# ---------------- Metrics ----------------
metrics_df = calculate_metrics(data)

if metrics_df.empty:
    st.error("Not enough data to calculate metrics.")
    st.stop()

# ---------------- KPI Cards ----------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("📈 Avg Return", f"{metrics_df['Return'].mean():.2f}%")
col2.metric("⚖️ Avg Risk", f"{metrics_df['Risk'].mean():.2f}%")

best_stock = metrics_df.loc[metrics_df["Return"].idxmax()]
col3.metric("🏆 Best Performer", best_stock["Asset"])

# ---------------- Price Trend ----------------
st.subheader("📊 Price Trends")

price_df = pd.DataFrame(data)
st.line_chart(price_df)

# ---------------- Returns Chart ----------------
st.subheader("📈 Returns Comparison")

fig_returns = px.bar(
    metrics_df,
    x="Asset",
    y="Return",
    color="Asset",
    text="Return",
    labels={"Return": "Return (%)"}
)
st.plotly_chart(fig_returns, use_container_width=True)

# ---------------- Risk vs Return ----------------
st.subheader("⚖️ Risk vs Return")

metrics_df["Size"] = metrics_df["Return"].apply(lambda x: max(abs(x), 1))

fig_risk = px.scatter(
    metrics_df,
    x="Risk",
    y="Return",
    text="Asset",
    size="Size",
    labels={"Risk": "Risk (%)", "Return": "Return (%)"}
)
st.plotly_chart(fig_risk, use_container_width=True)

# ---------------- Portfolio Pie ----------------
st.subheader("🟢 Portfolio Allocation")

portfolio_df = portfolio_pie(data)

fig_pie = px.pie(
    portfolio_df,
    names="Asset",
    values="Allocation",
    title="Equal Allocation Portfolio"
)
st.plotly_chart(fig_pie, use_container_width=True)

# ---------------- Insights ----------------
st.subheader("💡 Investment Insights")

for index, row in metrics_df.iterrows():
    if row["Risk"] > 25:
        risk_text = "🔴 High Risk"
    elif row["Risk"] > 15:
        risk_text = "🟡 Moderate Risk"
    else:
        risk_text = "🟢 Low Risk"

    st.write(
        f"**{row['Asset']}** → Return: {row['Return']:.2f}% | Risk: {row['Risk']:.2f}% → {risk_text}"
    )

st.info(f"💡 Insight: {best_stock['Asset']} is currently the best performer in your selection.")