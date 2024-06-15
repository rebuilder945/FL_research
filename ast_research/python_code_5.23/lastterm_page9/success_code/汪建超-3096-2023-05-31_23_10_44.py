#class Stock
class Stock:  
    """Stock Information Class"""
    def __init__(self,code,name,yesterdayprice="N/A",todayprice="N/A"):
        self.sCode = code
        self.sName = name
        self.PriceYesterday= yesterdayprice
        self.PeiceToday = todayprice
    def getCode(self):
        return self.sCode
    def  getName(self):
        return self.sName
    def getPriceYesterday(self):
        return self.PriceYesterday
    def getPriceToday(self):
        return self.PeiceToday
    def setPriceYesterday(self,price):
        self.PriceYesterday = price
    def getChangPercent(self):
        return (self.PriceToday - self.PeiceYesterday)%self.PriceYesterday


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


