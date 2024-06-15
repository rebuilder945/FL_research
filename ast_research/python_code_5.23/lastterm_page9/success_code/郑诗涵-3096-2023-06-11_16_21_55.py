#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,sCode,sName,yesterday,today):
        self.sCode=sCode
        self.sName=sName
        self.yesterday=yesterday
        self.today=today
    def getCode(self):
        return self.sCode
    def getName(self):
        return self.sName
    def getPriceYesterday(self):
        return self.PriceYesterday
    def getPriceToday(self):
        return self.PriceToday
    def setPriceYesterday(self,setPriceYesterday):
        return setPriceYesterday
    def getChangePercent(self):
        return ((self.getPriceYesterday())-50.25)/(self.setPriceYesterday(50.25))


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


