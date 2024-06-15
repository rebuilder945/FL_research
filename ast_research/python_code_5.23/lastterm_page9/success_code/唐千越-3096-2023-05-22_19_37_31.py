#class Stock
class Stock:
   def __init__(self,sCode,sName,priceYesterday,priceToday):
      self.__sCode = sCode
      self.__sName = sName
      self.__priceYesterday = priceYesterday
      self.__priceToday = priceToday
   def getCode(self):
      return self.__sCode
   def getName(self):
      return self.__sName
   def setPriceYesterday(self,priceYesterday):
      self.__PriceYesterday = priceYesterday
   def getPriceYesterday(self):
      return self.__PriceYesterday
   def setPriceToday(self,priceToday):
      self.__PriceToday = priceToday
   def getPriceToday(self):
      return self.__PriceToday
   def getChangePercentage(self):
      return (self.__priceToday - self.__priceYesterday) / self.__priceYesterday

      


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


