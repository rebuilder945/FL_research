#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def getCode(self):
        return self.a
    def getName(self):
        return self.b
    def getPriceYesterday(self):
        return self.c
    def getPriceToday(self):
        return self.d
    def setPriceYesterday(self,c):
        self.c=c
    def getChangePercent(self):
        return (self.d-self.c)/self.c



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


