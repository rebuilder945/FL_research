#class Stock
    def __init__(self,dai,ming,qian,xian):
        self.dai=dai
        self.ming=ming
        self.qian=qian
        self.xian=xian
    def getname(self):
        return self.ming
    def getdaima(self):
        return self.dai
    def getqian(self):
        return self.qian
    def setqian(self,yesterday):
        self.qain=yesterday
    def getxian(self):
        return self.xian
    def setxian(self,today):
        self.xian=today
    def getChangePercent(self):
        return (self.xian-self.qian)/self.qian


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


