#class Stock
class Stock:
&#160;&#160;&#160;&#160;"Stock Information Class"
&#160;&#160;&#160;&#160;def __init__(self,code,name,priceYesterday,priceToday):
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;self.__code = code
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;self.__name = name
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;self.__priceYesterday = priceYesterday
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;self.__priceToday = priceToday
&#160;&#160;&#160;&#160;def getName(self):
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;return self.__name &#160;&#160;&#160;
&#160;&#160;&#160;&#160;def getCode(self):
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;return self.__code
&#160;&#160;&#160;&#160;def getPriceYesterday(self):
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;return self.__priceYesterday
&#160;&#160;&#160;&#160;def setPriceYesterday(self,price):
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;self.__priceYesterday = price
&#160;&#160;&#160;&#160;def getPriceToday(self):
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;return self.__priceToday
&#160;&#160;&#160;&#160;def setPriceToday(self,price):
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;self.__priceToday = price
&#160;&#160;&#160;&#160;def getChangePercent(self):
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;return (self.__priceToday - self.__priceYesterday)/self.__priceYesterday



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


