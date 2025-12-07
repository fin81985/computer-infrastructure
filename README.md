# FAANG Stock Data Analysis

**Author:** Finian Doonan  

---

##  Project Overview

This project automates the download, analysis, and visualization of **FAANG stock data** (Facebook/META, Apple, Amazon, Netflix, Google) using Python.  

It demonstrates:  
- Data collection with [`yfinance`](https://pypi.org/project/yfinance/)  
- Data manipulation with [`pandas`](https://pandas.pydata.org/)  
- Visualization with [`matplotlib`](https://matplotlib.org/)  
- Automation with **GitHub Actions**


---

##  Features

- Automated hourly stock data download for the last 5 days  
- Timestamped CSV storage for version tracking  
- Line plots of FAANG closing prices in a single figure  
- Scheduled automated execution with GitHub Actions  

---

##  Installation

### Clone the repository:

```bash
git clone https://github.com/fin81985/faang-stock-analysis.git
cd faang-stock-analysis
```

### Create and activate a virtual environment:
````bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
````

### Install dependencies:

````bash
pip install -r requirements.txt
````
### Quick Start

Run the main script to download data and generate plots:
````bash
python faang.py
````

### Outputs:

| Folder | Content                                        |
| ------ | ---------------------------------------------- |
| data/  | Timestamped CSV files of FAANG stock data      |
| plots/ | Timestamped line plots of stock closing prices |


### Example filenames:

* CSV: 20251115-083012.csv

* Plot: 20251115-083245.png

 ## Data Structure

CSV files include the following columns:

| Column    | Description                       |
| --------- | --------------------------------- |
| Open      | Opening price of the stock        |
| High      | Highest price during the interval |
| Low       | Lowest price during the interval  |
| Close     | Closing price                     |
| Adj Close | Adjusted closing price            |
| Volume    | Number of shares traded           |
| Ticker    | Stock symbol                      |


## Visualization Example

````python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/20251115-083012.csv", index_col=0, parse_dates=True)
tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]

plt.figure(figsize=(12,6))
for ticker in tickers:
    stock_data = df[df['Ticker'] == ticker]
    plt.plot(stock_data.index, stock_data['Close'], label=ticker)

plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.title("FAANG Stock Prices")
plt.legend()
plt.show()
````

## Automation with GitHub Actions

* Schedule: Every weekday at 16:00 UTC or on push to main

* Workflow: **.github/workflows/faang.yml**

### Tasks automated:

* Download stock data

* Generate timestamped CSVs

* Create plots

* Upload artifacts

Learn more about [GitHub Actions](https://docs.github.com/en/actions)

## References

* [yfinance Documentation](https://pypi.org/project/yfinance/)

* [Matplotlib Documentation](https://matplotlib.org/stable/users/index.html)

* [Pandas Documentation](https://pandas.pydata.org/docs/)

* [GitHub Actions Documentation](https://docs.github.com/en/actions)

* [Python datetime Documentation](https://docs.python.org/3/library/datetime.html)


