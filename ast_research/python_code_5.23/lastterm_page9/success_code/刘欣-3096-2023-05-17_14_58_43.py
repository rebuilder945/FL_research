#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.__code__=sCode
        self.__name__=sName
        self.__py__=priceYesterday
        self.__pt__=priceToday
    def getName(self):
        return self.__name__
    def getCode(self):
        return self.__code__
    def getpy(self):
        return self.__py__
    def getpt(self):
        return self.__pt__
    def setpy(self,priceYesterday):
        self.__py__=priceYesterday
    def setpt(self,priceToday):
        self.__pt__=priceToday
    def getChangePercent(self):
        return "%.2f%"%((self.__pt__-self.__py__)/self.__py__*100)


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


