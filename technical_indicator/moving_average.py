
def sma(df, days, col="Close", start=0):
    """
    sma = (Sum of Period Values / Number of Periods)
    :param df: data frame
    :param days: days to calculate ema
    :param col: Data frame column use for calculating ema
    :param start: start day
    :return:
    """
    df['{}days_sma'.format(days)] = ""
    if df.shape[0] > days:
        for i in range(days, (df.shape[0] + 1)):
            df['{}days_sma'.format(days)][i - 1] = df.iloc[start:i, df.columns.get_loc(col)].sum(axis=0) / days
            start = start + 1
    else:
        print("Data is not sufficient to calculate {} SMA".format(days))


def ema(df, days, col="Close", start=0):
    """
    EMA = Closing price x multiplier + EMA (previous day) x (1-multiplier)
    For the first EMA, we use the SMA(previous day) instead of EMA(previous day).
    multiplier=[2 ÷ (number of observations + 1)]
    :param df: data frame
    :param days: days to calculate ema
    :param col: Data frame column use for calculating ema
    :param start: start day
    :return:
    """
    if df.shape[0] > days:
        multiplier = 2 / (days + 1)
        first_ema = df.iloc[:days, df.columns.get_loc(col)].sum(axis=0) / days
        df['{}days_ema'.format(days)] = ""
        df['{}days_ema'.format(days)][days - 1] = first_ema
        for i in range(days, (df.shape[0])):
            EMA = df.iloc[i, df.columns.get_loc(col)] * multiplier + df.iloc[
                (i - 1), df.columns.get_loc("{}days_ema".format(days))] * (1 - multiplier)
            df['{}days_ema'.format(days)][i] = EMA
            df['{}days_ema'.format(days)][i] = EMA
            start = start+1
    else:
        print("Not Sufficient data")



