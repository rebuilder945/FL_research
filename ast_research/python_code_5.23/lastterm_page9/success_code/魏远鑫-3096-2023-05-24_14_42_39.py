#class Stock
class Stock:
    def __init__(self,Code,Name,PriceYesterday,PriceToday):
        self.Code=sCode
        self.Name=sName
        self.PriceYesterday=priceYesterday
        self.PriceToday=priceToday
    def getCode(self):
        return self.Code
    def getName(self):
        return self.Name
    def getPriceYesterday(self):
        return self.PriceYesterday
    def getPriceToday(self):
        return self.PriceToday



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


