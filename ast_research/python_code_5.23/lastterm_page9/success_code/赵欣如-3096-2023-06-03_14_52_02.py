#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,code,name,priceyesterday,pricetoday):
        self.sCode=code
        self.sName=name
        self.priceYesterday=priceyesterday
        self.PriceToday=pricetoday
    def getCode(self):
        return(self.sCode)
    def getName(self):
        return(self.sName)
    def getPriceYesterday(self):
        return(self.priceYesterday)
    def getPriceToday(self):
        return(self.PriceToday)
    def getChangePercent(self):
        return((self.PriceToday-50.25)/50.25)
    def setPriceYesterday(self,Price):
        return(Price)


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


