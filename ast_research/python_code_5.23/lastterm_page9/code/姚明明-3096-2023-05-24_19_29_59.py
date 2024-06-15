#class Stock
class Stock:
    "Stock Information Class"
    def_init_(self,code,name,priceYesterday,priceToday):
        self._code=code
        self._name=name
        self._priceYesterday=priceYesterday
        self._priceToday=priceToday
    def getName(self):
        return self._name
    def getCode(self):
        return self._code
    def getPriceYestoday(self):
        return self._priceYestoday
    def setPriceYestoday(self,price):
        self._priceYestoday=price
    def getPriceToday(self):
        return self._priceToday
    def setPriceToday(self,price):
        self._priceToday=price



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


