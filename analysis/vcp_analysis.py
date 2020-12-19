import yfinance as yf
import pandas as pd
from technical_indicator import technical_indicator
import datetime as dt
# import numpy as np
from data_extract import symbol_extract

file_path = "../data/ind_niftynext50list.csv"

symbol_list = symbol_extract.extract_symbol(file_path)
# print(len(symbol_list))

count = 0
for i in symbol_list:
    try:

        df = yf.download("{}.NS".format(i), period="max", interval="1mo")
        df.dropna(inplace=True)
        # df.loc[:, 'sma50dv'] = technical_indicator.sma(df.Close, timeperiod=50)
        # df["50SMA > VW"] = (df.sma50dv > df.Volume)
        High_max = max(df.iloc[-30:-1]["High"])
        Low_min = min(df.iloc[-30:-1]["Low"])
        Diff_HL = (High_max-Low_min)/Low_min
        # High_mean = df.iloc[-6: ]["High"].mean()
        # Low_mean = df.iloc[-6: ]["Low"].mean()
        # Diff_HL = (High_mean-Low_mean)/Low_mean
        if Diff_HL > 0.10:
            continue

        else:
            df["Price Diff((H-L)/L)"] = (df["High"] - df["Low"]) / df["Low"]
            df["Price Contraction"] = np.where(df["Price Diff((H-L)/L)"] <= 0.1, True, False)
            alist = list(df.iloc[-6:]["Price Contraction"] == True)
            # blist = list(df.iloc[-30:]["10SMA > VW"] == True)
            if alist.count(True) >= 3:
                print("Stock is going throgh Price Contraction")
                #     df.to_excel("{}_analyse.xlsx".format(ticker), index=True)
                print(i)
                count = count +1
    except Exception as e:
        print("Exceptioin ", e)
        print(i)
print(count)





