#class Stock
class Stock:
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.sCode=code
        self.sName=name
        self.priceYesterday=yesprice
        self.priceToday=todprice
    def getCode(self):
        return code
    def getName(self):
        return name
    def getPriceYesterday(self):
        return yesprice
    def getPriceToday(self):
        return todprice
    def getChangePercent(self):
        return (yesprice+todprice)/todprice
    __doc__="Stock Information Class"



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


