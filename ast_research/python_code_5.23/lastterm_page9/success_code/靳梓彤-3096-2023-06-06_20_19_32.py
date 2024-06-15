#class Stock
class Stock:
    def __init__(self,fCode,sName,fPriceYesterday,fPriceToday):
        self.fCode =fCode
        self.sName =sName
        self.fPriceYesterday =fPriceYesterday
        self.fPriceToday =fPriceToday
    def getName(self):
        return self.sName    
    def getCode(self):
        return self.fCode
    def getPriceYesterday(self):
        return self.fPriceYesterday
    def setPriceYesterday(self,price):
        self.fPriceYesterday = price
    def getPriceToday(self):
        return self.fPriceToday
    def setPriceToday(self,price):
        self.fPriceToday = price
    def getChangePercent(self):
        return (self.fPriceToday - self.fPriceYesterday)/self.fPriceYesterday



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


