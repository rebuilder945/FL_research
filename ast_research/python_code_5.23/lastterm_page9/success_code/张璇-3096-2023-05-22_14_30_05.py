#class Stock
class Stock:
    def __init__ (self,code,name,PriceYesterday,PriceToday):
        self.code=sCode
        self.name=sName
        self.PriceYesterday=priceYesterday
        self.PriceToday=priceToday
    
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.PriceYesterday
    def getPriceToday(self):
        return self.PriceToday
    def setPriceYesterday(self):
        self.edit=50.25
    def getChangePercent(self):
        return (self.PriceToday-50.25)/50.25



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


