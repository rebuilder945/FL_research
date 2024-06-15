#class Stock
class  Stock:
    def __init__(self,daima,mingcheng,qian,hou):
        self.daima=daima
        self.mingcheng=mingcheng
        self.qian=qian
        self.hou=hou
    def getCode(self):
        return self.daima
    def getName(self):
        return self.mingcheng
    def getPriceYesterday(self):
        return self.qian
    def getPriceToday(self):
        return self.hou
    def setPriceYesterday(self,ee):
        self.vb=(self.hou-ee)/ee
    def getChangePercent(self):
        return self.vb


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


