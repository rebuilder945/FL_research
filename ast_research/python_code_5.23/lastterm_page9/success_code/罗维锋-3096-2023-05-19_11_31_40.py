#class Stock
class Stock:
    """Stock Information Class"""
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.c=sCode
        self.n=sName
        self.y=priceYesterday
        self.t=priceToday
    def getCode(self):
        return self.c
    def getName(self):
        return self.n
    def getPriceYesterday(self):
        return self.y
    def getPriceToday(self):
        return self.t
    def setPriceYesterday(self,a):
        self.y=a
    def getChangePercent(self):
        return (self.t-self.y)/self.y
    def setPriceToday(self,b):
        self.t=b


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


