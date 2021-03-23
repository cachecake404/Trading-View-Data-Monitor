import pychrome

class DataScrapper:
    def __init__(self):
        # There exists multiple HTML div with class label valueValue-3kA0oJs5 containing price and indicator data we need.
        # The class ID valueValue-3kA0oJs5 could potentially change in future which will break this code!
        self.classDataID = "valueValue-2KhwsEwE"
        # Calling document.getElemntByClassName on page returns a list of all the HTML div.
        # This variable indexMapping will contain the mapping between index and price or indicator data.
        self.indexMapping = {"price":5,"indicator":8}
        # Port You Opened Up Remote Chrome Debugging
        self.port = "9222"
        # Connct to Chrome
        self.setUpPyChrome()

    # Sets up the connection to Chrome using Chrome Remote Debugging.
    # Refer the tutorial at https://blog.chromium.org/2011/05/remote-debugging-with-chrome-developer.html
    def setUpPyChrome(self):
        browser = pychrome.Browser(url="http://127.0.0.1:{}".format(self.port))
        self.tab = browser.list_tab()[0]
        self.tab.start()

    # Function that leverages TradingView HTML structure to get the data desired!
    def getRawData(self,classID,indexLocation):
        commandToExecute = "customData=document.getElementsByClassName(\"{}\")[{}]".format(classID,indexLocation)
        dataDiv = self.tab.Runtime.evaluate (expression=commandToExecute,executionContextId=1)
        data = self.tab.Runtime.evaluate(expression="customData.innerText",executionContextId=1)["result"]["value"]
        return float(data)

    # Returns the Price
    def getPrice(self):
        return self.getRawData(self.classDataID,self.indexMapping["price"])


    # For all Indicator from 1 to N
    # Returns the value for the indicator number specified.
    def getIndicator(self,indicatorNumber):
        return self.getRawData(self.classDataID,self.indexMapping["indicator"]+indicatorNumber-1)
