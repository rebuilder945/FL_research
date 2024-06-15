#class Stock
calss Stock:
    "Stock Information Class"
    def __init__(self,sName,sCode,PricreYesterday,PriceToday):
        self.name=sName
        self.code=sCode
        self.priceyesterday=PriceYesterday
        self.pricetoday=PriceToday
    def getName(self):
        return self.name
    def getCode(self):
        return self.code
    def getPriceYesterday(self):
        return self.priceyesterday
    def getPriceToday(self):
        return self.pricetoday
    def setPriceYesterday(self, PriceYesterday):
        self.priceyesterday=PriceYesterday
    def setPriceToday(self, PriceToday):
        self.pricetoday=PriceToday
    def getChangePercent(self):
        return ((PriceYesterday-PriceToday)/PriceYesterday)



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


