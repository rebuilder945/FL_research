#class Stock
    'Stock Information Class'
    def __init__(self,sid='000000',sname='N/A',s1='N/A',s2='N/A'):
        self.id=sid
        self.name=sname
        self.s1=s1
        self.s2=s2
    def getCode(self):
        return self.id
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.s1
    def getPriceToday(self):
        return self.s2
    def setPriceYesterday(self,n1):
        self.s1=n1
    def getChangePercent(self):
        return (self.s2-self.s1)/self.s1


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


