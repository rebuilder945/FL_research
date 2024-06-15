#class Stock
class Stock:    
    "Stock Information Class"
    def __init__(self,a,b,c,d):
        self.code=a
        self.name=b
        self.ppy=float(c)
        self.ppp=float(d)

    def getCode(self):
        return self.code

    def getName(self):
        return self.name

    def getPriceYesterday(self):
        return self.ppy

    def getPriceToday(self):
        return self.ppp

    def getChangePercent(self):
        return self.p
    
    def setPriceYesterday(self,n):
        self.p=(self.ppp-n)/n
  


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


