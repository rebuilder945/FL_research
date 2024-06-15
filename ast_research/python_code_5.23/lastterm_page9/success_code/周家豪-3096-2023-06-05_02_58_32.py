#class Stock
class Stock:
    "Stock Information Class"
    def __init__(self,code,name,pry,prt):
        self.code=code
        self.name=name
        self.pry=pry
        self.prt=prt
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.pry
    def getPriceToday(self):
        return self.prt
    def setPriceYesterday(self,a):
        self.pry=a
    def setPriceToday(self,a):
        self.prt=a
    def getChangePercent(self):
        return (self.prt-self.pry)/self.prt


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


