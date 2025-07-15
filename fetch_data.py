# Task 1: Fetch data from Yahoo Finance

# install pandas: pip install pandas
# install yfinance: pip install yfinance

import pandas as pd
import yfinance as yf

def fetch_save_data(ticker = "GOOG", start ="2020-01-01", end = "2024-12-31"):
    df = yf.download(ticker, start = start, end = end)
    df.to_csv("C:/Users/user/Desktop/Sunway/MST3074 Machine Learning for Data Mining/googleproject/data/google_raw.csv")

if __name__ == '__main__':
    fetch_save_data()