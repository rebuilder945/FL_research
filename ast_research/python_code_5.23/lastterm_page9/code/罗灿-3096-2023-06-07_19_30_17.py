#class Stock
    "Stock Information Class"
    def __init__(self,id,name,Yprice,Tprice):
        self.sid=id
        self.sname=name
        self.sYprice=Yprice
        self.sTprice=Tprice

    def getname(self):
        return self.sname

    def getid(self):
        return self.sid
    
    def getYprice(self):
        return self.sYprice

    def setYprice(self,price):
        self.sYprice=price

    def getTprice(self):
        return self.sTprice

    def setTprice(self,price):
        self.sTprice=price

    def getChangePercent(self):
        return (self.sTprice-self.sYprice)/self.sYprice


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


