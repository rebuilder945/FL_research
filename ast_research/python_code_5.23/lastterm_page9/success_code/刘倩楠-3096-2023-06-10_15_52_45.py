#class Stock
def __init__(self,sCode,sName,priceYesterday,priceToday):
    self.Name=sName
    slef.Code=sCode
    self.priceyesterday=priceYesterday
    self.pricetoday=priceToday

def getName(self):
    return self.Name

def getCode(self):
    return self.code

def getPriceYesterday(self):
    return self.priceyesterday

def getPriceToday(self):
    return self.pricetoday

def getChangePercent(self):
    return float(self.priceyesterday/self.pricetoday)


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


