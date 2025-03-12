import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Pull in data and convert it to a pandas dataframe

df = pd.read_csv('aapl_stock_prices.csv', delimiter=',')
print(df.columns)

dates = df['Date']
prices = df['Close']
highs = df['High'] 
lows = df['Low']
opens = df['Open']
closes = df['Close']


# Calculate a 20-day moving average
df["MA20"] = df["Close"].rolling(window=20).mean()

# Create a candlestick chart
fig, ax = plt.subplots(figsize=(12, 6), facecolor="black")

# Plot the OHLC data as a candlestick chart manually
# We'll use a loop and identify each candlestick as either red or green
# loc is label-based indexing, iloc is integer-based indexing


for i in range(len(df)):
    color = "green" if df["Close"].iloc[i] > df["Open"].iloc[i] else "red"
    ax.plot([df.index[i], df.index[i]], [df["Low"].iloc[i], df["High"].iloc[i]], color=color, linewidth=1)  # Wicks
    ax.plot([df.index[i], df.index[i]], [df["Open"].iloc[i], df["Close"].iloc[i]], color=color, linewidth=4)  # Body

# Plot the moving average
ax.plot(df.index, df["MA20"], color="white", lw=2, linestyle="dashed", label="20-day MA")

# Set labels, title, and styling
ax.set_facecolor("black")
ax.spines["top"].set_color("white")
ax.spines["bottom"].set_color("white")
ax.spines["left"].set_color("white")
ax.spines["right"].set_color("white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.tick_params(colors="white")
ax.legend(facecolor="black", edgecolor="white")
ax.set_title("Apple", color="white")


plt.show()



# Create a line chart with a 20-day moving average

fig, ax = plt.subplots(figsize=(12, 6), facecolor="black")

ax.plot(df.index, df["Close"], color="blue", lw=2, label="Close Price")
ax.plot(df.index, df["MA20"], color="yellow", lw=2, linestyle="dashed", label="20-day MA")

# Set labels, title, and styling
ax.set_facecolor("black")
ax.spines["top"].set_color("white")
ax.spines["bottom"].set_color("white")
ax.spines["left"].set_color("white")
ax.spines["right"].set_color="white"
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.tick_params(colors="white")
ax.legend(facecolor="black", edgecolor="white")
ax.set_title("20-day Moving Average", color="white")

# Show the chart
plt.show()
