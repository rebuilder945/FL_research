#class Stock
Class Stock：
    "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.sCode=sCode
        self.sName=sName
        self.priceYesterday=priceYesterday
        self.priceToday=priceToday

    def getCode(self):
        return self.sCode
 
    def getName(self):
        return self.sName
    
    def getPriceYesterday(self):
        return self.priceYesterday

    def setPriceYesterday(self,setPriceYesterday):
        return setPriceYesterday

    def getPriceToday(self):
        return self.priceToday

    def setpriceToday(self,setpriceToday):
        return setpriceToday

    def getChangePercent(self):
        return float((self.getPriceToday()-self.setPriceYesterday(50.25))/self.setPriceYesterday(50.25))


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

