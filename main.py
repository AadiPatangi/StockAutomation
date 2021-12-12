import yfinance as yf
import climage


#Apple Holdings
AppleIMG = climage.convert('apple.png') #read the image
print(AppleIMG) 

apple = yf.download('AAPL', period = '1d')
print(apple)
print("******************************")
#DowJones Holdings
DJIMG = climage.convert('dowjones.png') 
print(DJIMG) 

DowJones = yf.download('QQQM', period = '1d')
print(DowJones)
print("******************************")

#BMW Holdings
BMWIMG = climage.convert('bmw.png') #read the image
print(BMWIMG) 

bmw = yf.download('BMWYY', period = '1d')
print(bmw)