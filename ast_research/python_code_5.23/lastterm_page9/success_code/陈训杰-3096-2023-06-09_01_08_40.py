#class Stock
class Stock:
    def __init__(self,code,name,yesd_price,tod_price):
        self.__code = code                      #__私有
        self.__name = name
        self.__yesd_price = yesd_price
        self.__tod_price = tod_price
    def getCode(self):          #代码
        return self.__code
    def getName(self):          #名字
        return self.__name
    def getPriceYesterday(self):                #前一天
        return self.__yesd_price
    def setPriceYesterday(self,new_price):      #更新
        self.__yesd_price = new_price
    def getPriceToday(self):                    #今天
        return self.__tod_price
    def setPriceToday(self,new_price):          #更新
        self.__tod_price = new_price
    def getChangePercent(self):
        return (self.__tod_price - self.__yesd_price) / self.__yesd_price
    __doc__ = 'Stock Information Class'


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


