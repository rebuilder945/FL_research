#class Stock

    __code = 0
    __name = ""
    __priceYesterday = 0.0
    __priceToday = 0.0
    __doc__ = "Stock Information Class"
    def __init__ (self, code, name, priceYesterday, priceToday):
        Stock.__code = code
        Stock.__name = name
        Stock.__priceYesterday = priceYesterday
        Stock.__priceToday = priceToday

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getPriceYesterday(self):
        return self.__priceYesterday

    def getPriceToday (self):
        return self.__priceToday

    def setCode(self, code):
        self.__code = code

    def getChangePercent (self):
        return (self.__priceToday - self.__priceYesterday) / self.__priceYesterday

    def setName(self, name):
        self.__Name = name

    def setPriceYesterday (self, priceYesterday):
        self.__priceYesterday = priceYesterday

    def setPriceToday (self, priceToday):
        self.__priceToday (priceToday):


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


