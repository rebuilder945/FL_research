#class Stock
class Stock:
    """
    This class represents a stock.

    Attributes:
    - Code (str): The code of the stock.
    - Name (str): The name of the stock.
    - Price/Yesterday (float): The price of the stock at the end of the previous trading day.
    - Price/Today (float): The price of the stock at the current trading day.
    """

    def __init__(self, Code, Name, Price/Yesterday, Price/Today):
        self.Code = code
        self.Name = name
        self.Price/Yesterday = Price/Yesterday
        self.Price/Today = Price/Today
    
    def getCode(self):
        return self.Code
    
    def getName(self):
        return self.Name
    
    def getPrice/Yesterday(self):
        return self.Price/Yesterday
    
    def getPrice/Today(self):
        return self.Price/Today
    
    def setPrice/Yesterday(self, newPrice/Yesterday):
        self.Price/Yesterday = newPrice/Yesterday
    
    def getChangePercent(self):
        return (self.Price/Today - self.Price/Yesterday) / self.Price/Yesterday
    



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


