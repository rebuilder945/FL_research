#class Stock
calss Stock:
    "Stock Information Class"
    def __init__(self,sName="N/A",sCode="N/A",priceYesterday=0,priceToday=0):
        self.name=sName
        self.code=sCode
        self.priceYesterday=priceYesterday
        self.priceToday=priceToday
    def getName(self):
        return str(self.name)
    def getCode(self):
        return str(self.code)
    def getPriceYesterday(self):
        return float(self.priceYesterday)
    def getPriceToday(self):
        return float(self.priceToday)
    def setPriceYesterday(self, setPriceYesterday):
        return float(setPriceYesterday)
    def setPriceToday(self, setPriceToday):
        return float(setPriceToday)
    def getChangePercent(self):
        return float((s.getPriceToday()-s.setPriceYesterday(50.25))/s.setPriceYesterday(50.25))



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


