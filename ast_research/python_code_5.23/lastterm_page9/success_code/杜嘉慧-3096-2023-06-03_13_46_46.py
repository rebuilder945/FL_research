#class Stock
class Stock:
    '''Stock Information Class'''
    def __init__(self, scode, sname, fpricey, fpricet):
        self.code = scode
        self.name = sname
        self.priceyes = fpricey
        self.priceto = fpricet
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.priceyes
    def getPriceToday(self):
        return self.priceto
    def setPriceYesterday(self, new):
        self.priceyes = new
    def getChangePercent(self):
        return (self.priceto - self.priceyes) / self.priceyes


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


