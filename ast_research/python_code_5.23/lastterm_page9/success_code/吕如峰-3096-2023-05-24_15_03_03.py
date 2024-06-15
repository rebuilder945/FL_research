#class Stock
def __init__(self):
    self.symbol = ""
    self.name = ""
    self.previousClosingPrice = 0
    self.currentPrice = 0
def creatStock(self,stockInfo):
    self.symbol = stockInfo[0]
    self.name = stockInfo[1]
    self.previousClosingPrice = stockInfo[2]
    self.currentPrice = stockInfo[3]
def getStockName(self):
    return(self.name)
def getStockNo(self):
    return(self.symbol)
def setPreviousClosingPrice(self,price):
    self.previousClosingPrice = price
def getPreviousClosingPrice(self):
    return(self.previousClosingPrice)
def setCurrentPrice(self,price):
    self.currentPrice = price
def getCurrentPrice(self):
    return(self.currentPrice)
def getChangePercent(self):
    return((self.currentPrice - self.previousClosingPrice)/self.currentPrice)

INTC = Stock()
INTC.creatStock(["000001","Intel Corporation",20.5,20.35])
print(INTC.getStockNo())
print(INTC.getStockName())
print(INTC.getCurrentPrice())
print(INTC.getPreviousClosingPrice())
print("%.2f%%" % (INTC.getChangePercent()*100))



sCode = input() #Stock Code
sName = input() #Stock Name
priceYesterday = float(input())  #Price/Yesterday
priceToday = float(input())  #Price Today
s = Stock(sCode,sName,priceYesterday,priceToday)
print("Code:",s.getCode())
print("Name:",s.getName())
print("Price/Yesterday:%.2f\nPrice Today:%.2f" % (s.getPriceYesterday(),s.getPriceToday()))
s.setPriceYesterday(50.25)
print("Edit Price/Yesterday To:%.2f" % 50.25)
print("Price Change Percentage:%.2f%%" % (s.getChangePercent()*100))
print(Stock.__doc__)


