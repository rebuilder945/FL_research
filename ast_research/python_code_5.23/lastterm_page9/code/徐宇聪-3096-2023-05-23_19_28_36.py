#class Stock
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.code = sCode
        self.name = sName
        self.priceYesterday = priceYesterday
        self.pricetoday = priceToday

    def __getCode__(self):
        return self.code
    
    def __getName__(self):
        return self.name
    
    def __getPriceYesterday__(self):
        return self.priceYesterday
    
    def __getPriceToday__(self):
        return self.pricetoday
    
    def __setPriceYesterday__(self,ee):
        self.vb = (self.priceYesterday - ee) / ee

    def __getChangePercent__(self):
        return self.vb


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


