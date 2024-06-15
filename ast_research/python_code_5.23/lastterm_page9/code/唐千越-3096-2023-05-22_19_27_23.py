#class Stock
class Stock:
   def __init__(self,sc,sn,py,pt):
      self.__sCode = sc
      self.__sName = sn
      self.__princeYesterday = py
      self.__princeToday = pt
   def getCode(self):
      return self.__sCode
   def getName(self):
      return self.__sName
   def getPriceYesterday(self):
      return self.__PriceYesterday
   def getPriceToday(self):
      return self.__PriceToday
    def setPriceYesterday(self,py):
      self.__PriceYesterday = py
    def setPriceToday(self,pt):
      self.__PriceToday = pt
    def getChange Percentage(self):
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


