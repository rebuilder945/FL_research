#class Stock
    "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        s.sCode=sCode
        s.sName=sName
        s.priceYesterday=priceYesterday
        s.priceToday=priceToday
    def getCode(self):
        return s.sCode
    def getName(self):
        return s.sName
    def getPriceYesterday(self):
        return s.PriceYesterday
    def getPriceToday(self):
        return s.PriceToday
    def setPriceYesterday(self,price):
        s.priceYesterday=price
    def getChangePercent(self):
        return (s.priceToday-s.priceYesterday)/s.priceYesterday



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


