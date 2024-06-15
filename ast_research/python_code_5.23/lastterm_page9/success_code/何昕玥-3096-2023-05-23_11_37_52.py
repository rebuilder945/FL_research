#class Stock
class Stock:
         """Stock Information Class"""
         def _init_(self,sCode,sName,priceYesterday,priceToday):
               self._sCode=sCode
               self._sName=sName
               self._priceYesterday=priceYesterday
               self._priceToday=priceToday
         def getsName(self):
               return self._sName
         def getsCode(self):
               return self._sCode
         def getpriceYesterday(self):
               return self._priceYesterday
         def setpriceYesterday(self,priceYesterday):
               self._priceYesterday=priceYesterday
         def getpriceToday(self):
               return self._priceToday
         def setpriceToday(self,priceToday):
               self._priceToday=priceToday
         def getChangePercent(self):
               return (self._priceToday-self._priceYesterday)/self._priceYesterday



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


