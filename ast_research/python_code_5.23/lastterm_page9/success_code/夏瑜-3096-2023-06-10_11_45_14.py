#class Stock
class  Stock:
    "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.__scode=sCode
        self.__sname=sName
        self.__priceYesterday=priceYesterday
        self.__priceToday=priceToday
    def getCode(self):
        return self.__scode
    def getName(self):
        return self.__sname
    def getPriceYesterday(self):
        return self.__priceYesterday
    def getPriceToday(self):
        return self.__priceToday
    def setPriceYesterday(self,PriceYesterday):
        self.__priceYesterday=priceYesterday
    def setPriceToday(self,PriceToday):
        self.__priceToday=priceToday
    def getChangePercent(self):
        return   (self.__priceYesterday - self.__priceToday)/self.__priceToday


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


