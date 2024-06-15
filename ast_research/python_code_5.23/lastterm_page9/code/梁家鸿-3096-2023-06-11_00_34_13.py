#class Stock
class Stock    
    "Stock Information Class."
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.code = sCode
        self.name = sName
        self.pricey = priceYesterday
        self.pricet = priceToday
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def sgetPriceYesterday(self):
        return self.pricey
    def getPriceToday(self):
        return self.pricet
    def getChangePercent(self):
        ChangePercent = (self.pricet-self.pricey)/self.pricey
        return ChangePercent
    def setPriceYesterday(pricey):
        return pricey
sCode  =  input()  #Stock  Code


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


