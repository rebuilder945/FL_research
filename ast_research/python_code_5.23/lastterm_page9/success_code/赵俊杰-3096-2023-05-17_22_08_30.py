#class Stock
class  Stock:    
    """Stock Information Class"""
    def __init__(self,Code,Name,YPrice,TPrice):
        self.sCode=Code
        self.sName=Name
        self.sYPrice=YPrice
        self.STPrice=TPrice
    def getCode(self):
        return self.sCode
    def getName(self):
        return self.sName
    def setPriceYesterday(self,n):
        self.sYPrice=n
    def getPriceToday(self):
        return self.STPrice
    def getPriceYesterday(self):
        return self.sYPrice
    def getChangePercent(self):
        return (self.STPrice-self.sYPrice)/self.sYPrice
        


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


