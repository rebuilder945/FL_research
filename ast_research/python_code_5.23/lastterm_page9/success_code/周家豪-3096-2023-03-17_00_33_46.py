#class Stock
class  Stock:
    "Stock Information Class"
    def __init__(self,code,name,priceyesterday,pricetoday):
        self._code=code
        self._name=name
        self._priceyesterday=priceyesterday
        self._pricetoday=pricetoday
    def getCode(self):
        return self._code
    def getName(self):
        return self._name
    def getPriceYesterday(self):
        return self._priceyesterday
    def getPriceToday(self):
        return self._pricetoday
    def setPriceYesterday(self, price):
        self._priceyesterday = price
    def getChangePercent(self):
        return (self._pricetoday-self._priceyesterday)/self._priceyesterday


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


