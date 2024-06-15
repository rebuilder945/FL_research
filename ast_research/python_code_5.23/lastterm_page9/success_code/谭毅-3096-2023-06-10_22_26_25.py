#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,sCode='a',sName='a',priceYesterday='a',priceToday='a'):
        self.scode=sCode
        self.sname=sName
        self.priceyesterday=priceYesterday
        self.pricetoday=priceToday
    def getCode(self):
        return self.scode
    def getName(self):
        return self.sname
    def getPriceYesterday(self):
        return self.priceyesterday
    def getPriceToday(self):
        return self.pricetoday
    def setPriceYesterday(self,a):
        self.priceyesterday=a
        return '%.2f'%self.priceyesterday
    def setPriceToday(self,a):
        self.pricetoday=a
        return '%.2f'%self.pricetoday
    def getChangePercent(self):
        b=(self.pricetoday-self.priceyesterday)/self.priceyesterday
        return b


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


