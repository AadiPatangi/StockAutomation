import yfinance as yf



#Apple Holdings
apple = yf.download('AAPL', period = '1d')

print(apple)
print("******************************")
#DowJones
DowJones = yf.download('QQQM', period = '1d')

print(DowJones)
