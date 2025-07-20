import yfinance as yf
import shutil
from datetime import datetime

def update_logo():
    # Fetch last two days' market data for S&P 500
    ticker = '^GSPC'
    data = yf.download(ticker, period='2d')

    if data.empty or len(data) < 2:
        print("Not enough market data.")
        return

    yesterday_close = data['Close'][-2]
    today_close = data['Close'][-1]

    # Decide which logo to use based on market direction
    if today_close >= yesterday_close:
        # Market up or flat -> use green
        shutil.copy('public/macroscope-green.png', 'public/logo.png')
        print("Market is up or flat — using green logo.")
    else:
        # Market down -> use burgundy
        shutil.copy('public/macroscope-burgundy.png', 'public/logo.png')
        print("Market is down — using burgundy logo.")

if __name__ == "__main__":
    update_logo()
