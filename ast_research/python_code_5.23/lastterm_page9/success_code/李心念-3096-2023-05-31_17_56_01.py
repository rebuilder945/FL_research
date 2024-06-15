#class Stock
class Stock:
    def __init__(self,code,name,priceY,priceT):
        self.getCode=code
        self.getName=name
        self.getPriceYesterday=priceY
        self.getPriceToday=priceT
    def setPriceYesterday(self,a):
        self.getPriceYesterday=a
    def getChangePercent(self):
        return (self.getPriceToday-self.getPriceYesterday)/self.getPriceYesterday
    print("Stock Information Class")


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


