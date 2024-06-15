#class Stock
def __init__(self):
        self.sCode  = ""
        self.sName = ""
        self.priceYesterday = 0
        self.priceToday = 0
def Stock(self,stockInfo):
        self.sCode  = stockInfo[0]
        self.sName = stockInfo[1]
        self.priceYesterday = stockInfo[2]
        self.priceToday = stockInfo[3]
def getStockName(self):
        return(self.sName )
def getStockNo(self):
        return(self.sCode)
def setpriceYesterday(self,price):
        self.priceYesterday = price
def getpriceYesterday(self):
        return(self.priceYesterday)
def setpriceToday (self,price):
        self.priceToday  = price
def getpriceToday (self):
        return(self.priceToday )
def getChangePercent(self):
        return((self.priceToday  - self.priceYesterday)/self.priceToday )



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


