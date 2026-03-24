import yfinance as yf
import pandas as pd
import numpy as np

def fetch_stock_data(tickers, period="1y"):
    """
    Fetch historical close prices for given tickers.
    Returns a dictionary of DataFrames.
    """
    data = {}
    for t in tickers:
        try:
            ticker_data = yf.Ticker(t).history(period=period)["Close"]
            data[t] = ticker_data
        except:
            print(f"Could not fetch data for {t}")
    return data

def calculate_metrics(data):
    """Calculate annualized return (%) and risk (annual volatility %) for each asset."""
    metrics = []
    for asset, df in data.items():
        if len(df) == 0:
            continue  # skip empty data
        returns = ((df[-1] - df[0]) / df[0]) * 100
        volatility = np.std(df.pct_change().dropna()) * np.sqrt(252) * 100
        metrics.append({"Asset": asset, "Return": returns, "Risk": volatility})
    return pd.DataFrame(metrics)

def portfolio_pie(data):
    """
    Create a simple portfolio allocation (equal investment in selected assets)
    """
    num_assets = len(data)
    allocation = {asset: 100/num_assets for asset in data.keys()}
    return pd.DataFrame(list(allocation.items()), columns=["Asset","Allocation"])