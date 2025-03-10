import yfinance as yf 
import pandas as pd 

"""
Description: get_dataset.py fetches 1 year of OHLC price data 
from the ticker 
ticker_info = data.get_info()
print(ticker_info)

keys = ticker_info.keys()
print(dir(data))
"""


def get_price_history(ticker):
    d = yf.Ticker(ticker)
    price_history = d.history(period="1y")
    df = pd.DataFrame(price_history)
    return df



prices = get_price_history('AAPL')

# Save DataFrame to CSV in the 'data' directory
prices.to_csv("data/aapl_stock_prices.csv", index=True)

print("Stock prices saved to data/aapl_stock_prices.csv")  







