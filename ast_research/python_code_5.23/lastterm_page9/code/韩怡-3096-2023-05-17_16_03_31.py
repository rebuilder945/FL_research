#class Stock
    "Stock Information Class"
    def __init__(self,code,name,yesterday,today):
        self.code=code
        self.name=name
        self.yesterday=yesterday
        self.today=today
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.yesterday
    def getPriceToday(self):
        return self.today
    def setPriceYesterday(self,n):
        self.yesterday=n
    def getChangePercent(self):
        return (self.today-self.yesterday)/self.yesterday


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


