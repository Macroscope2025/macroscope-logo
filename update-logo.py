import yfinance as yf
from datetime import datetime, timedelta
import shutil

# Config
UP_IMAGE = "macroscope-green.png"
DOWN_IMAGE = "macroscope-burgundy.png"
OUTPUT_IMAGE = "logo.png"
MARKET = "^GSPC"  # S&P 500

def get_previous_market_close():
    today = datetime.now()
    offset = 1 if today.weekday() > 0 else 3  # Adjust for Monday (gets Friday)
    prev_day = today - timedelta(days=offset)
    return prev_day.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d')

def is_market_up():
    start, end = get_previous_market_close()
    data = yf.download(MARKET, start=start, end=end)
    if data.empty or "Close" not in data.columns:
        raise ValueError("Market data unavailable")
    close_values = data["Close"].values
    return close_values[-1] > close_values[0]

def update_logo():
    source = UP_IMAGE if is_market_up() else DOWN_IMAGE
    shutil.copyfile(source, OUTPUT_IMAGE)
    print(f"Logo updated to {source}")

if __name__ == "__main__":
    update_logo()
