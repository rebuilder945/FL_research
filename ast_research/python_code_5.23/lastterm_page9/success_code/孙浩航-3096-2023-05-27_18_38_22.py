#class Stock
class Stock:
    def __init__(self,code,name,price1,price2):
        self.code=code
        self.name=name
        self.price1=price1
        self.price2=price2
    

    def getCode(self):
        return self.code

    def getName(self):
        return self.name

    def getPriceYesterday(self):
        return self.price1

    def setPriceYesterday(self, price):
        self.price1 = price

    def getPriceToday(self):
        return self.price2

    def getChangePercent(self):
        return (self.price2 - self.price1) / self.price1


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


