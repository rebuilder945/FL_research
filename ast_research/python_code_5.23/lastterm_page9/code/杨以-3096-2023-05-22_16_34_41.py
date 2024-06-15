#class Stock
    '''Stock Information Class'''

    def __init__(self,scode,sname,fpriyes,fprito):
        self.code=scode
        self.name=sname
        self.priyes="%.2f"%fpriyes
        self.prito='%.2f'%fprito
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.priyes
    def setPriceYesterday(self,n):
        self.priyes="%.2f"%n
    def getPriceToday(self):
        return self.prito
    def setPriceToday(self,n):
        self.prito="%.2f"%n
    def getChangePercent(self):
        return "%.2f"%((self.prito-self.priyes)/sel


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


