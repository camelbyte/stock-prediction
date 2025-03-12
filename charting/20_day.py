import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv('data/aapl_stock_prices.csv', delimiter=',')
print(df.columns)

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
