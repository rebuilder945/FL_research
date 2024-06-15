#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,Code,Name,priceYesterday,priceToday):
        self.Code=Code
        self.Name=Name
        self.priceYesterday=priceYesterday
        self.priceToday=priceToday
    def getName(self):
        return self.Name
    def getCode(self):
        return self.Code
    def getpriceYesterday(self):
        return self.priceYesterday
    def setpriceYesterday(self,price):
        self.priceYesterday = price
    def getpriceToday(self):
        return self.priceToday
    def setpriceToday(self,price):
        self.priceToday = price
    def getChangePercent(self):
        return (self.priceToday-self.priceYesterday)/self.priceYesterday



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


