#class Stock
class Stock:
    def __init__(self,Code,name,lprice,nprice):
        self.Code=Code
        self.Name=name
        self.lprice=lprice
        self.nprice=nprice
    def getName(self):
        return self.Name
    def getCode(self):
        return self.Code
    def getPriceYesterday(self):
        return self.lprice
    def getPriceToday(self):
        return self.nprice
    def getChangePercent(self):
        return (self.nprice-self.lprice)/self.lprice


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


