#class Stock
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.__scode = sCode
        self.__sname = sName
        self.__priceyesterday = priceYesterday
        self.__pricetodat = priceToday
    def getCode(self):
        return self.__scode
    def set_scode(self,scode):
        self.__scode = scode
    def getName(self):
        rerurn self.__sname
    def set_sname(self,sname):
        self.__sname = sname
    def getPriceYesterday(self):
        return self.__priceyesterday
    def set_priceyesterday(self,priceyesterday):
        self.__priceyesterday = priceyesterday
    def getPriceToday(self):
        return self.__pricetoday
    def set_pricetoday(self,pricetoday):
        self.__pricetoday = pricetoday
    def setPriceYesterday(self,newy):
        self.__priceyesterday = newy
    def getChangePercent(self):
        return (self.__pricetoday - self.__priceyesterday) / self.__priceyesterday


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


