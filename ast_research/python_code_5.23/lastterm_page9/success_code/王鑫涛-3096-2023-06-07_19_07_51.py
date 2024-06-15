#class Stock
class Stock:
    def __init__(self,code='N/A',name='N/A',priceyesterday=0,pricetoday=0):
        self.sName=name
        self.sCode=code
        self.priceYesterday=float(priceYesterday)
        self.priceToday=float(priceToday)
    def getCode(self):
        return self.sCode
    def getName(self):
         return self.sName
    def getPriceYesterday(self):
        return self.priceYesterday
    def getPriceToday(self):
        return self.priceToday
    def setPriceYesterday(self,a):
        self.priceYesterday=float(a)
    def setPriceToday(self,b):
        self.pricecToday=float(b)
    def getChangePercent(self):
        m=(self.priceToday-self.priceYesterday)/self.priceYesterday
        return m


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


