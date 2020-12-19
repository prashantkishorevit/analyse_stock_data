import yfinance as yf
import pandas as pd
from technical_indicator import moving_average as ma
from data_extract import symbol_extract

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option("mode.chained_assignment", None)


file_path = "./data/ind_nifty50list.csv"

symbol_list = symbol_extract.extract_symbol(file_path) # Extract stock symbol

stock_above_sma= [] # Creating empty list

for i in symbol_list:
    try:
        df = yf.download("{}.NS".format(i), period="1y", interval="1d") # Extract last 1yr daily stock data
        df.dropna(inplace=True)
        ma.sma(df, days=200) # calling SMA function
        current_closing_price = df["Close"][-1] # current day closing price
        current_sma = df["200days_sma"][-1] # current day 200D SMA
        if current_closing_price > current_sma:
            stock_above_sma.append(i)
    except Exception as e:
        print("Exceptioin ", e)

print("list of stocks moving above 200 days SMA:", stock_above_sma)
print(len(stock_above_sma))