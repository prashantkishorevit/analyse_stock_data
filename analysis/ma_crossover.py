import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
from technical_indicator import moving_average as ma


pd.options.display.float_format = '{:,.2f}'.format
pd.set_option("mode.chained_assignment", None)

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
ticker = "YESBANK.NS"
df = yf.download(ticker,period="10y",interval="1d")