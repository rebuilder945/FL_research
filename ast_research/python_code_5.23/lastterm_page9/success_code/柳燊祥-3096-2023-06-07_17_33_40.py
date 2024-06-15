#class Stock
class Stock:
    def __init__(self,sCode="N/A",sName="N/A",priceYestoday=0,priceToday=0):
        self.sCode=sCode
        self.sName=sName
        self.priceYestoday=priceYestoday
        self.priceToday=priceToday
    def getCode(self):
        return str(self.sCode)
    def getName(self):
        return str(self.sName)
    def getPriceYestoday(self):
        return float(self.priceYestoday)
    def setPriceYestoday(self,setPriceYestoday):
        return float(setPriceYestoday)
    def getPriceToday(self):
        return float(self.priceToday)
    def getChangePercent(self):
        return float((s.getPriceToday()-s.setPriceYestoday(50.25))/s.setPriceYestoday(50.25))


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


