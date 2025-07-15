import pandas as pd
import mplfinance as mpf

def plot_candlestick(csv_path="C:/Users/user/Desktop/Sunway/MST3074 Machine Learning for Data Mining/googleproject/data/google_raw.csv"):
    df = pd.read_csv(csv_path, index_col = 0, parse_dates = True)
    mpf.plot(df, type = "candle", volume = True, style = 'yahoo', savefig = 'C:/Users/user/Desktop/Sunway/MST3074 Machine Learning for Data Mining/googleproject/images/candlestick.png')

if __name__ == '__main__':
    plot_candlestick()