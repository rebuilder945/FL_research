#class Stock
    "Stock Information Class"
    def __init__(self,code,name,priceYesterday,priceToday):
        self.__code = code
        self.__name = name
        self.__priceYesterday = priceYesterday
        self.__priceToday = priceToday
    def getName(self):
        return self.__name    
    def getCode(self):
        return self.__code
    def getPriceYesterday(self):
        return self.__priceYesterday
    def setPriceYesterday(self,price):
        self.__priceYesterday = price
    def getPriceToday(self):
        return self.__priceToday
    def setPriceToday(self,price):
        self.__priceToday = price
    def getChangePercent(self):
        return (self.__priceToday - self.__priceYesterday)/self.__priceYesterday


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


