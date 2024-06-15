#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,code,name,pricey,pricet):
        self.__code=code
        self.__name=name
        self.__pricey=pricey
        self.__pricet=pricet
    def getCode(self):
        return self.__code
    def getName(self):
        return self.__name
    def getPriceYesterday(self):
        return self.__pricey
    def getPriceToday(self):
        return self.__pricet
    def setPriceYesterday(self,val):
        self.__pricey=val
    def setPriceToday(self,val):
        self.__pricet=val
    def getChangePercent(self):
        return self.__pricet/self.__pricey-1



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


