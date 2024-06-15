#class Stock
class Stock:
    def __init__(self, Code, Name, priceYesterday,priceToday):
        self.sCode = Code
        self.sName = Name
        self.spriceYesterday = priceYesterday
        self.spriceToday = priceToday
    def getCode(self):
        return self.sCode
    def getName(self)：
        return self.sName
    def getpriceYesterday(self):
        return self.spriceYesterday
    def getpriceToday(self):
        return self.spriceToday
    def setpriceToday(self, new):
        self.priceToday = new
    def setpriceYesterday(self, new):
        self.priceYesterday = new
    def getChangePercent(self):
        return (self.spriceToday-self.spriceYesterday)/self.spriceYesterday


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


