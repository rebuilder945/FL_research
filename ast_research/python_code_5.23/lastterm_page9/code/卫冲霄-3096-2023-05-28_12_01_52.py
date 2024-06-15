#class Stock
    "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.sCode=sCode
        self.sName=sName
        self.priceYesterday=priceYesterday
        self.priceToday=priceToday
    def getName(self):
        return self.sName
    def getCode(self):
        return self.sCode
    def getPriceYesterday(self):
        return priceYesterday
    def setPriceYesterday(self,priceYesterday):
        self.priceYesterday=priceYesterday
    def getPriceToday(self):
        return priceToday
    def setPriceToday(self,priceToday):
        self.priceToday=priceToday
    def getChangePercent(self):
        return (self.priceToday-self.priceYesterday)/self.priceToday


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


