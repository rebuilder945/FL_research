#class Stock
class Stock:
    '''Stock Information Class
    '''
    def __init__(self,cod,nam,yespri,todpri):
        self.code=cod
        self.name=nam
        self.yesterday_price=yespri
        self.today_price=todpri
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def getPriceYesterday(self):
        return self.yesterday_price
    def getPriceToday(self):
        return self.today_price
    def setPriceYesterday(self,n):
        self.yesterday_price=n
    def setPriceToday(self,n):
        self.today_price=n
    def getChangePercent(self):
        return -(self.yesterday_price-self.today_price)/self.yesterday_price


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


