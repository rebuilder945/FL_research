#class Stock
class Stock:
    "user defined class:Stock"
    def __init__(self,StockCode,StockName,PriceYesterday,PriceToday) :
        self.sCode=StockCode
        self.sName=StockName
        self.priceyesterday=PriceYesterday
        self.pricetoday=PriceToday
    def getCode(self):
        return self.sCode
    def getName(self):
        return    self.sName
    def getPriceYesterday(self):
        return    self.priceyesterday
    def  getPriceToday(self):
        return   self.pricetoday
    def setPriceYesterday(self,n):
        self.priceyesterday=n
        return      self.priceyesterday
    def setPriceTOday(self,n):
        self.pricetoday=n
        return self.pricetoday
    def getChangePercent(self):
        m=(self.pricetoday-self.priceyesterday)/self.priceyesterday
        return m 
def __doc__ ():
    a="Stock Information Class"
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


