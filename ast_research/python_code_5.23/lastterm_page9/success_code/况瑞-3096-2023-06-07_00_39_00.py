#class Stock
class Stock:
    "Stock Information Class"
    
    def __init__(self,a,b,c,d):
        self.code=a
        self.name=b
        self.py=c
        self.pt=d
        self.m=0
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.py
    def getPriceToday(self):
        return self.pt
    def setPriceYesterday(self,e):
        self.m+=e
       
        
    
    def getChangePercent(self):
        return (self.pt-self.m)/self.m       


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


