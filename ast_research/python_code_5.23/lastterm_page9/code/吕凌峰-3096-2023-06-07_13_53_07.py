#class Stock
     "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.code=sCode
        self.name=sName
        self.priceyesterday=priceYesterday
        self.pricetoday=priceToday
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.priceyesterday
    def getPriceToday(self):
        return self.pricetoday
    def setPriceYesterday(self,iset):
        self.setprice=iset
    def getChangePercent(self):
        ichange=(self.pricetoday-self.setprice)/self.setprice
        return ichange


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


