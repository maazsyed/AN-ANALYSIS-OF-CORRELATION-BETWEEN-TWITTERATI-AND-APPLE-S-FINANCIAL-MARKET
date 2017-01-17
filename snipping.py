from yahoo_finance import Share
from pprint import pprint

nintendo = Share('NTDOY')
print ("get_open: ", nintendo.get_open())
print ("get_price: ", nintendo.get_price())
print ("get_trade_datetime: ", nintendo.get_trade_datetime())


# Historical data
pprint (nintendo.get_historical('2016-04-25', '2016-09-24'))