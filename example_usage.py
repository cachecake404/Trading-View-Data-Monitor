# Example 1: Print Out All Scrapable Data

from TradingViewDataGetter import DataScrapper
dataHandler = DataScrapper()

price = dataHandler.getPrice()
ema200 = dataHandler.getIndicator(1)
ema20 = dataHandler.getIndicator(2)
rsi = dataHandler.getIndicator(3)

print("Here is your data:")
print("Price: {}, EMA200: {}, EMA 20: {}, RSI: {}".format(price,ema200,ema20,rsi))

# Example 2: Print All Scrapable Data Every Second for 2 Minutes

print("\nGoing to print data every second now for 2 minutes!\n")
import time

timeOutSeconds = 120
tickSeconds = 1

while(timeOutSeconds!=0):
    timeOutSeconds -= 1
    price = dataHandler.getPrice()
    ema200 = dataHandler.getIndicator(1)
    ema20 = dataHandler.getIndicator(2)
    rsi = dataHandler.getIndicator(3)
    print("Price: {}, EMA200: {}, EMA 20: {}, RSI: {}".format(price,ema200,ema20,rsi))
    time.sleep(tickSeconds)
    
