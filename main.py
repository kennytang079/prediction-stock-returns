import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# #Downloaded the data
# apple = yf.download("AAPL", start="2020-01-01", end="2025-01-01")
# apple["Return"]= apple["Close"].pct_change()

# print(apple.head())

# #Plot of Stock Prices
# apple["Close"].plot(figsize=(12,6))
# plt.title("Apple Stock Price")
# plt.xlabel("Date")
# plt.ylabel("Price")
# plt.show()

# #Plot of Stock Returns
# apple["Return"].plot(figsize=(12,6))
# plt.title("Apple Daily Return")
# plt.xlabel("Date")
# plt.ylabel("Daily Return")
# plt.show()

# #Statistics
# print(apple["Return"].mean())
# print(apple["Return"].std())

# apple["Return"].hist(bins=50)
# plt.title("Distribution of Apple Return")
# plt.xlabel("Daily Returns")
# plt.ylabel("Frequency")
# plt.show()


# #Rolling Statistics
# apple["Rolling Volatility"] = apple["Return"].rolling(window=30).std()
# apple["Rolling Volatility"].plot(figsize=(12,6))
# plt.title("Apple 30 Day Rolling Volatility")
# plt.xlabel("Date")
# plt.ylabel("Volatility")
# plt.show()

# apple["MA30"] = apple["Close"].rolling(window=30).mean()
# apple["MA100"] = apple["Close"].rolling(window=100).mean()
# apple["Close"].plot(figsize=(12,6), label="Close Price")
# apple["MA30"].plot(label="30 day MA")
# apple["MA100"].plot(label="100 day MA")

# plt.title("Apple Price with Moving Averages")
# plt.xlabel("Date")
# plt.ylabel("Price")
# plt.legend()
# plt.show()

# #Prediction Statistics
# apple["Signal"] = (apple["MA30"] > apple["MA100"]).astype(int)
# apple["Signal"].plot(figsize=(12,4))

# plt.title("Trend Signal")
# plt.xlabel("Date")
# plt.ylabel("Signal")
# plt.show()

# apple["Future Return"] = apple["Return"].shift(-1)
# bullish_return = apple[apple["Signal"]==1]["Future Return"]
# bearish_return = apple[apple["Signal"]==0]["Future Return"]
# print(bullish_return.mean())
# print(bearish_return.mean())

# #Hypothesis Testing
# t_stat, p_value = ttest_ind(
#     bullish_return.dropna(),
#     bearish_return.dropna(),
#     equal_var=False,
# )
# print("T Statistic", t_stat)
# print("P Value", p_value)


tickers = [
    "AAPL",   # Technology
    "MSFT",   # Technology
    "NVDA",   # Semiconductors
    "AMZN",   # Consumer
    "GOOGL",  # Communication Services
    "META",   # Social Media
    "JPM",    # Banking
    "XOM",    # Energy
    "JNJ",    # Healthcare
    "WMT"     # Retail
]

results = []

for ticker in tickers:
    data = yf.download(
        ticker,
        start="2020-01-01", 
        end="2025-01-01"
    )
    data["Return"] = data["Close"].pct_change()
    data["MA30"] = data["Close"].rolling(30).mean()
    data["MA100"] = data["Close"].rolling(100).mean()

    data["Signal"] = (
        data["MA30"] > data["MA100"]
        ).astype(int)

    data["FutureReturn"] = data["Return"].shift(-1)

    bullish_returns = data[data["Signal"] == 1]["FutureReturn"]

    bearish_returns = data[data["Signal"] == 0]["FutureReturn"]

    t_stat, p_value = ttest_ind(
        bullish_returns.dropna(),
        bearish_returns.dropna(),
    equal_var=False
    )

    results.append({
        "Ticker": ticker,
        "Bull Mean": bullish_returns.mean(),
        "Bear Mean": bearish_returns.mean(),
        "T Statistic": t_stat,
        "P Value": p_value
    })

results_df = pd.DataFrame(results)
results_df = results_df.sort_values(by="P Value")

print(results_df)


