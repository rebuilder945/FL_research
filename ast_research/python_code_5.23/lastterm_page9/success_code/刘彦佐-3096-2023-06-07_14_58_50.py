#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,sc,sn,py,pt):
        self.sCode=sc
        self.sName=sn
        self.priceYesterday=py
        self.priceToday=pt
    def getName(self):
        return self.sName
    def getCode(self):
        return self.sCode
    def setPriceYesterday(self,py):
        self.priceYesterday=py
    def getPriceYesterday(self):
        return self.priceYesterday
    def setPriceToday(self,pt):
        self.priceToday=pt
    def getPriceToday(self):
        return self.priceToday
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


