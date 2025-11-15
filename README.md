# FAANG Stock Data Analysis

**Module:** Principles of Data Analytics  
**Author:** [Your Name]

This project automates the download, analysis, and visualization of **FAANG stock data** (Facebook/META, Apple, Amazon, Netflix, Google) using Python libraries such as [yfinance](https://pypi.org/project/yfinance/), [Pandas](https://pandas.pydata.org/), and [Matplotlib](https://matplotlib.org/). The goal is to demonstrate data collection, exploration, visualization, and automation with **GitHub Actions**.

The full code is implemented in the [faang.py](faang.py) script, which downloads data, saves CSV files, and generates plots automatically.

---

## Libraries Used

```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

---

* yfinance
: Download historical stock data from Yahoo Finance.

Pandas
: Data manipulation and analysis library.

* Matplotlib
: Plotting library for creating static visualizations.

* datetime: Handles timestamps for file naming.

* os & glob: File system operations for creating folders and retrieving the latest data files.

---

Task 1: Download FAANG Data

* Download hourly stock data for the previous 5 days.

* Stocks: META, AAPL, AMZN, NFLX, GOOG

* Saves each dataset as a timestamped CSV in the data/ folder.

* Example filename: 20251115-083012.csv

Reference: yfinance documentation [https://pypi.org/project/yfinance/]

---

Task 2: Explore Data Structure