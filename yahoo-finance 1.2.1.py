# https://pypi.python.org/pypi/yahoo-finance

# Get shares data
# Nintendo Co. Ltd. (NTDOY)
import yahoo as yahoo
from yahoo_finance import Share

# yahoo = Share('YHOO')

apple = Share('AAPL')
# print ("get_open: ", apple.get_open())
# print ("get_price: ", apple.get_price())
# print ("get_trade_datetime: ", apple.get_trade_datetime())

# Refresh data from market
apple.refresh()
# print ("get_price: ", apple.get_price())
# print ("get_trade_datetime: ", apple.get_trade_datetime())

# Historical data
# print yahoo.get_historical('2014-04-25', '2014-04-29')
# print (nintendo.get_historical('2016-04-25', '2016-09-24'))

# More readable output :)
from pprint import pprint
# pprint(yahoo.get_historical('2014-04-25', '2014-04-29'))
pprint (apple.get_historical('2016-10-22', '2016-10-30'))

# import csv
# with open('apple.csv', 'w') as csvfile:
#     fieldnames = ['Adj_Close', 'Close', 'Date', 'High', 'Low', 'Open', 'Symbol', 'Volume']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for row in apple.get_historical('2016-10-22', '2016-10-30'):
#         writer.writerow(row)
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})

# Summary information for our example
# pprint(yahoo.get_info())
# pprint(apple.get_info())

# Avalible methods
#
# get_price()
# get_change()
# get_volume()
# get_prev_close()
# get_open()
# get_avg_daily_volume()
# get_stock_exchange()
# get_market_cap()
# get_book_value()
# get_ebitda()
# get_dividend_share()
# get_dividend_yield()
# get_earnings_share()
# get_days_high()
# get_days_low()
# get_year_high()
# get_year_low()
# get_50day_moving_avg()
# get_200day_moving_avg()
# get_price_earnings_ratio()
# get_price_earnings_growth_ratio()
# get_price_sales()
# get_price_book()
# get_short_ratio()
# get_trade_datetime()
# get_historical(start_date, end_date)
# get_info()
# refresh()