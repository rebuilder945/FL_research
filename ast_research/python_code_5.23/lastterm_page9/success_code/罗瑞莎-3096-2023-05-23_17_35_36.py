#class Stock
class Stock:
    def __init__(s,code,name,pricey,pricet):
        s.Code = code
        s.Name = name
        s.PriceYesterday = pricey
        s.PriceToday = pricet

    def getCode(s):
        return s.Code

    def getName(s):
        return s.Name
        
    def getPriceYesterday(s):
        return s.PriceYesterday

    def getPriceToday(s):
        return s.PriceToday

    def setPriceYesterday(s,price):
        s.PriceYesterday = price

    def getChangePercent(s):
        return (PriceToday-PriceYesterday)/PriceToday

    def __doc__(self):
        return("Stock Information Class")


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


