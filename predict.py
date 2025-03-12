import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
from datetime import datetime


df = pd.read_csv('charting/aapl_stock_prices.csv', delimiter=',')

print(df.sample(5))
print(df.columns)
print(df.describe())


