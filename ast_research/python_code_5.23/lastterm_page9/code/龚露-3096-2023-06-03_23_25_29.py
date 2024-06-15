#class Stock
calss Stock:
    "Stock Information Class"
    def __init__(self,sName="N/A",sCode="N/A",PricreYesterday=0,PriceToday=0):
        self.name=sName
        self.code=sCode
        self.PriceYesterday=PriceYesterday
        self.PriceToday=PriceToday
    def getName(self):
        return self.name
    def getCode(self):
        return self.code
    def getPriceYesterday(self):
        return self.PriceYesterday
    def getPriceToday(self):
        return self.PriceToday
    def setPriceYesterday(self, PriceYesterday):
        self.PriceYesterday=PriceYesterday
        return self.PriceYesterday
    def setPriceToday(self, PriceToday):
        self.PriceToday=PriceToday
        return slef.PriceToday
    def getChangePercent(self):
        return (s.getPriceToday()-s.PriceYesterday(50.25))/s.setPriceYesterday(50.25)



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


