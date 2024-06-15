#class Stock
class Stock:    
    def __init__(self,code,Name,t_price,y_price):
        self.code=code
        self.Name=Name
        self.tp=t_price
        self.yp=y_price
    def getCode(self):
        return self.code 
    def getName(self):
        return self.Name
    def getPriceYesterday(self):
        return self.yp 
    def setPriceYesterday(self,price):
        self.yp=price
    def getPriceToday(self):
        return self.tp 
    def setPriceToday(self,price):
        self.tp=price
    def getChangePercent(self):
        return (self.tp-self.yp)/(self.yp)


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


