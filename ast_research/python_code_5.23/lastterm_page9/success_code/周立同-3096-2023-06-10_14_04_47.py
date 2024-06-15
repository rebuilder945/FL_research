#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,sCode="N/A",sName="N/A",priceYesterday="N/A",priceToday="N/A"):
        self.code=sCode
        self.name=sName
        self.pry=priceYesterday
        self.prt=priceToday
    def getCode(self):
        return self.code   
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.pry
    def getPriceToday(self):
        return self.prt
    def setPriceYesterday(self,setpr):
        self.setPriceYesterday=setpr
    def getChangePercent(self):
        per=(self.prt-self.setPriceYesterday)/self.setPriceYesterday
        return per


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


