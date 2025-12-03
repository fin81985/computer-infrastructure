

def plot_data():
    """
    Downloads the latest Close prices for multiple tickers using yfinance.Tickers,
    plots them on a single chart, and saves the plot to the 'plots' folder with
    a timestamped filename for GitHub Actions use.
    """

    # --- Create timestamp for file naming ---
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")

    # --- Ensure 'plots' directory exists ---
    os.makedirs("plots", exist_ok=True)

    # --- Tickers to fetch ---
    tickers_str = "MSFT AAPL AMZN NFLX GOOG"

    # --- Fetch data using yfinance ---
    tickers = yf.Tickers(tickers_str)
    data = tickers.history(period="1mo")   # Last month of data
    close_prices = data["Close"]

    # --- Create the plot ---
    plt.figure(figsize=(12, 6))

    for ticker in close_prices.columns:
        plt.plot(close_prices.index, close_prices[ticker], label=ticker)

    plt.title("Close Prices for Multiple Tickers")
    plt.xlabel("Date")
    plt.ylabel("Close Price (USD)")
    plt.legend()
    plt.grid(True)

    # --- Save timestamped plot ---
    filename = f"close_prices_{timestamp}.png"
    plot_path = os.path.join("plots", filename)
    plt.savefig(plot_path)

    # Clean up for headless GitHub Actions environment
    plt.close()

    print(f"Plot saved to {plot_path}")


if __name__ == "__main__":
    plot_data()