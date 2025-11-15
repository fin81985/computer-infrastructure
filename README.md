# FAANG Stock Data Analysis

**Module:** Computer Infrastructure 
**Author:** Finian Doonan

This project automates the download, analysis, and visualization of **FAANG stock data** (Facebook/META, Apple, Amazon, Netflix, Google) using Python libraries such as [yfinance](https://pypi.org/project/yfinance/), [Pandas](https://pandas.pydata.org/), and [Matplotlib](https://matplotlib.org/). The goal is to demonstrate data collection, exploration, visualization, and automation.

The full code is implemented in the [faang.py](faang.py) script, which downloads data, saves CSV files, and generates plots automatically.

---

## Libraries Used

```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

```

---

* yfinance: Download historical stock data from Yahoo Finance.

* Pandas: Data manipulation and analysis library.

* Matplotlib: Plotting library for creating static visualizations.

* datetime: Handles timestamps for file naming.

* os & glob: File system operations for creating folders and retrieving the latest data files.

---

## Task 1: Download FAANG Data

* Download hourly stock data for the previous 5 days.

* Stocks: META, AAPL, AMZN, NFLX, GOOG

* Saves each dataset as a timestamped CSV in the data/ folder.

* Example filename: `20251115-083012.csv`

Reference: [yfinance documentation](https://pypi.org/project/yfinance/)

---

## Task 2: Explore Data Structure

* Columns in the dataset:
``Open, High, Low, Close, Adj Close, Volume, Ticker``

* Multiple stocks are combined into one DataFrame for easy plotting.

* CSV files are timestamped for version tracking.

```python
# Example: Viewing the first 5 rows
df = pd.read_csv("data/20251115-083012.csv")
print(df.head())

```

---

## Task 3: Visualize Stock Prices

* Created line plots of Close prices for all FAANG stocks in a single figure.

* Axis labels: Date (x-axis), Close Price in USD (y-axis)

* Legend: Stock tickers

* Title includes the date of the plot

* Saves plots as timestamped PNG in the plots/ folder.

* Example filename: 20251115-083245.png

```python
plt.plot(stock_data.index, stock_data['Close'], label=ticker)
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.title("FAANG Stock Prices - 2025-11-15")
plt.legend()
plt.savefig("plots/20251115-083245.png")

```
|Reference: [Matplotlib Line Plot Tutorial](https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html)
