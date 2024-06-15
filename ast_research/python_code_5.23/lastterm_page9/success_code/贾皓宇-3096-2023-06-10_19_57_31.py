#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.__code=sCode
        self.__name=sName
        self.__priceYesterday=priceYesterday
        self.__priceToday=priceToday
    def getName(self):
        return self.__name
    def getCode(self):
        return self.__code
    def setPriceYesterday(self,yestd):
        self.__priceYesterday=yestd
    def getPriceYesterday(self):
        return self.__priceYesterday
    def setPriceToday(self,td):
        self.__priceToday=td
    def getPriceToday(self):
        return self.__priceToday
    def getChangePercent(self):
        bh=(self.____priceToday-self.__priceYesterday)/self.__priceYesterday
        return bh


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


