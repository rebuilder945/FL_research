#class Stock
class Stock():
    """Stock Information Class"""
    def __init__(self,daima,mingcheng,zuotian,jintian):
        self.__daima = daima
        self.__mingcheng = mingcheng
        self.__zuotian = zuotian
        self.__jintian = jintian

    def getCode(self):
        return self.__daima
    def getName(self):
        return self.__mingcheng
    def getPriceYesterday(self):
        return self.__zuotian
    def getPriceToday(self):
        return self.__jintian
    def getChangePercent(self):
        return (self.__jintian - self.__zuotian)/(self.__zuotian)
    
    def setPriceYesterday(self,jiage):
        return self.__zuotian = jiage
    def setPriceToday(self,jiage):
        return self.__jintian = jiage



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


