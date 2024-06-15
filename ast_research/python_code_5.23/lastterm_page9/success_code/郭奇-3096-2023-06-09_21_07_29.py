#class Stock
class Stock:
    '''Stock Information Class
    '''
    def __init__(self,Code,Name,PriceYesterday,PriceToday):
        self.Code=Code
        self.Name=Name
        self.PriceYesterday=PriceYesterday
        self.PriceToday=PriceToday
    def getName(self):
        return self.Name
    def getCode(self):
        return self.Code
    def setPriceYesterday(self,PriceYesterday):
        self.PriceYesterday=PriceYesterday
    def getPriceYesterday(self):
        return self.PriceYesterday
    def setPriceToday(self,PriceToday):
        self.PriceToday=PriceToday
    def getPriceToday(self):
        return self.PriceToday
    def getChangePercent(self):
        return (self.PriceToday-self.PriceYesterday)/self.PriceYesterday
    def __doc__(self):
        return 'Stock Information Class'


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


