#class Stock
class Stock:

    "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.sCode = sCode
        self.sName = sName
        self.priceYesterday = priceYesterday
        self.priceToday = priceToday
    def getCode(self):
        return sCode
    def getName(self):
        return sName
    def getPriceYesterday(self):
        return priceYesterday
    def getPriceToday(self):
        return priceToday
    def setPriceYesterday(self,a):
        self.priceYesterday = a
    def getChangePercent(self):
        a = (self.priceToday-self.priceYesterday)/self.priceYesterday
        return a 


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


