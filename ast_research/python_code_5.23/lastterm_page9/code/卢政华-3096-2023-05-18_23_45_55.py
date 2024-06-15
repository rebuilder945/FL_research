#class Stock
    def __init__(self, code, name, priceYesterday, priceToday):
        self.__code = code
        self.__name = name
        self.__priceYesterday = priceYesterday
        self.__priceToday = priceToday
    def getCode(self):
        return self.__code
    def getName(self):
        return self.__name
    def getPriceYesterday(self):
        return self.__priceYesterday
    def setPriceYesterday(self, priceYesterday):
        self.__priceYesterday = priceYesterday
    def getPriceToday(self):
        return self.__priceToday
    def setPriceToday(self, priceToday):
        self.__priceToday = priceToday
    def getChangePercent(self):
        return (self.__priceToday - self.__priceYesterday) / self.__priceYesterday * 100


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

