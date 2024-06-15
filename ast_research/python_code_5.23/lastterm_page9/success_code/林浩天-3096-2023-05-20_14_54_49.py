#class Stock
class Stock:
    """
    This class represents a stock.

    Attributes:
    - code (str): The code of the stock.
    - name (str): The name of the stock.
    - priceYesterday (float): The price of the stock at the end of the previous trading day.
    - priceToday (float): The price of the stock at the current trading day.
    """

    def __init__(self, code, name, priceYesterday, priceToday):
        self.code = code
        self.name = name
        self.priceYesterday = priceYesterday
        self.priceToday = priceToday
    
    def getCode(self):
        return self.code
    
    def getName(self):
        return self.name
    
    def getPriceYesterday(self):
        return self.priceYesterday
    
    def getPriceToday(self):
        return self.priceToday
    
    def setPriceYesterday(self, newPriceYesterday):
        self.priceYesterday = newPriceYesterday
    
    def getChangePercent(self):
        return (self.priceToday - self.priceYesterday) / self.priceYesterday
    



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


