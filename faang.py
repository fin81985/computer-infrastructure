#!/usr/bin/env python3 

# Problem 3: Script
# Author: Finian Doonan

import os # https://docs.python.org/3/library/os.html
import yfinance as yf # https://pypi.org/project/yfinance/
import matplotlib.pyplot as plt # https://matplotlib.org/stable/index.html

def plot_data():
    """
    Downloads the latest Close prices for multiple tickers using yfinance.Tickers,
    plots them on a single chart, and saves the plot to the 'plots' folder.
    """
    # Ensure 'plots' directory exists
    os.makedirs("plots", exist_ok=True) # create plots directory if not exists
    # https://docs.python.org/3/library/os.html#os.makedirs
    
    
tickers_str = "MSFT AAPL AMZN NFLX GOOG" # define tickers string

# Fetch data using yfinance
get_data = yf.Tickers(tickers_str)
data = get_data.history(period="1mo")  # last month's data 


close_prices = data['Close'] # extract Close prices

 

 # Plotting the Close prices using matplotlib 
plt.figure(figsize=(12, 6))
    
for ticker in close_prices.columns:
        plt.plot(close_prices.index, close_prices[ticker], label=ticker)
plt.title("Close Prices for Multiple Tickers")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.legend()
plt.grid(True)

# show plot
plt.show()

# Save the plot
plot_path = os.path.join("plots", "close_prices_plot.png")
plt.savefig(plot_path)
plt.close()

print(f"Plot saved to {plot_path}")

if __name__ == "__main__": # https://docs.python.org/3/library/__main__.html
    plot_data()