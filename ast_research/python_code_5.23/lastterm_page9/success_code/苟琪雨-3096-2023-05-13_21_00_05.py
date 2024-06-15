#class Stock
class Stock:
    "Stock Information Class"
    def __init__(Stock,Code,Name,priceYesterday,priceToday):
        Stock.sCode=Code
        Stock.sName=Name
        Stock.priceYesterday=priceYesterday
        Stock.priceToday=priceToday
    def getCode(Stock):
        return Code
    def getName(Stock):
        return Name
    def getPriceYesterday(Stock):
        return priceYesterday
    def getPriceToday(Stock):
        return priceToday
    def setPriceYesterday(Stock,n):
        Stock.priceYesterday=n
    def getChangePercent(Stock):
        return (Stock.priceToday - Stock.priceYesterday) / Stock.priceYesterday


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


