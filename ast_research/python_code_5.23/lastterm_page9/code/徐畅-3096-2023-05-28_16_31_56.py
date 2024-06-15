#class Stock
class Stock:
    def __init__(self,code,name,preprice,nowprice):
        self.code=code
        self.name=name
        self.preprice=preprice
        self.nowprice=nowprice
    
    def getCode(self):
        return self.code
     
    def getName(self):
        return self.name
    
    def getPriceYesterday(self):
        return self.preprice
    
    def getPriceToday(self):
        return self.nowprice
    
    def setPriceYesterday(self,newprice):
        self.preprice=newprice

    def getChangePercent(self):
        a=(self.nowprice-self.preprice)/self.preprice
        return a

     "Stock Information Class"


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


