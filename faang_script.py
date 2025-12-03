import os
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt


def plot_data():
    """
    Downloads Close prices for several tickers using yfinance.Tickers,
    plots them on one chart, and saves the result to /plots
    using a UTC timestamped filename.
    """

    # --- Timestamp (UTC recommended for GitHub Actions consistency) ---
    timestamp = dt.datetime.utcnow().strftime("%Y%m%d-%H%M%S")

    # --- Ensure plots folder exists ---
    os.makedirs("plots", exist_ok=True)

    # --- FAANG + MSFT tickers ---
    tickers_str = "MSFT AAPL AMZN NFLX GOOG"

    try:
        # --- Download last month of price data ---
        tickers = yf.Tickers(tickers_str)
        data = tickers.history(period="1mo")

    except Exception as e:
        print(f"ERROR: Failed to download data: {e}")
        return

    # --- Extract close prices safely ---
    if "Close" not in data:
        print("ERROR: No 'Close' data returned from yfinance.")
        return

    close_prices = data["Close"]

    # --- Drop empty columns (common with yfinance) ---
    close_prices = close_prices.dropna(axis=1, how="all")

    if close_prices.empty:
        print("ERROR: No valid price data found.")
        return

    # --- Plot ---
    plt.figure(figsize=(12, 6))

    for ticker in close_prices.columns:
        plt.plot(close_prices.index, close_prices[ticker], label=ticker, linewidth=2)

    plt.title("Close Prices for FAANG + MSFT (Last 1 Month)")
    plt.xlabel("Date")
    plt.ylabel("Close Price (USD)")
    plt.legend()
    plt.grid(True)

    # --- Save the plot ---
    filename = f"close_prices_{timestamp}.png"
    save_path = os.path.join("plots", filename)

    plt.savefig(save_path, dpi=200, bbox_inches="tight")
    plt.close()

    print(f"Plot saved: {save_path}")

if __name__ == "__main__":
    plot_data()
