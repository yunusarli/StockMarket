import yfinance as yf

# get stock info
def info(name):
    name = name.upper()
    stock_name = yf.Ticker(name)
    stock_info = stock_name.info

    name = stock_info['shortName']
    description = stock_info['longBusinessSummary']
    price = stock_info['regularMarketPrice']
    open_price = stock_info['open']
    dayHigh = stock_info['dayHigh']
    dayLow = stock_info['regularMarketDayLow']
    previous_close = stock_info['previousClose']
    fifty_day_average = stock_info['fiftyDayAverage']
    two_hundred_day_average = stock_info['twoHundredDayAverage']
    fifty2_week_high = stock_info['fiftyTwoWeekHigh']
    fifty2_week_low = stock_info['fiftyTwoWeekLow']
    daily_volume = stock_info['regularMarketVolume']
    ten_day_volume = stock_info['averageDailyVolume10Day']

    infos = [name,description,price,open_price,dayHigh,dayLow,previous_close,fifty_day_average,two_hundred_day_average,fifty2_week_high,fifty2_week_low,daily_volume,ten_day_volume]
    return infos