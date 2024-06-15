#class Stock
"Stock Information Class"
def __init__(self,code,name,priceYestoday,priceToday):
    self.code=code
    self.name=name
    self.priceYestoday=priceYestoday
    self.priceToday=priceToday
def getName(self):
    return self.name
def getCode(self):
    return self.code
def getPriceYestoday(self):
    return self.priceYestoday

def setPriceYestoday(self,price):
    self.priceYestoday=price
def getPriceToday(self):
    return self.priceToday=priceToday
def setPriceToday(self,price):
    self.priceToday=price
def getChangePercent(self):
    a=(self.priceToday-self.priceYestoday)/self.priceYestoday
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


