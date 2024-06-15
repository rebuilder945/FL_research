#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.__Code = sCode
        self.__Name = sName
        self.__Yesterday = priceYesterday
        self.__Today = priceToday
    def getCode(self):
        return self.__Code
    def getName(self):
        return self.__Name
    def getPriceYesterday(self):
        return self.__Yesterday
    def getPriceToday(self):
        return self.__Today
    def setPriceYesterday(self,n:float):
        self.__Yesterday = n
        return self.__Yesterday
    def getChangePercent(self):
        a = (self.__Today - self.__Yesterday)/self.__Yesterday
        return a



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


