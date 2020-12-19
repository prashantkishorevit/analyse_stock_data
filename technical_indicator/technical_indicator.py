import talib

def sma(col, timeperiod):

    return talib.SMA(col, timeperiod)

def ema(col, timeperiod):
    return talib.EMA(col, timeperiod)


def rsi(col, timeperiod=14):
    return talib.RSI(col, timeperiod)

