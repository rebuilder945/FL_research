#class Stock
class Stock:
    'Stock Information Class'
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.daima = sCode
        self.name = sName
        self.preprice = priceYesterday
        self.nowprice = priceToday
    def getCode(self):
        return self.daima
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.preprice
    def getpriceToday(self):
        return self.nowprice
    def setPriceYesterday(self,new):
        self.preprice = new
    def setPriceToday(self,new):
        self.nowprice = new
    def getChangePercent(self):
        answer = (self.nowprice - self.preprice)/self.preprice
        return answer
   


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


