#class Stock
def __init__(self, symbol, name, price, volume):
        self.symbol = symbol
        self.name = name
        self.price = price
        self.volume = volume

def get_symbol(self):
        return self.symbol

def get_name(self):
        return self.name

def get_price(self):
        return self.price

def get_volume(self):
        return self.volume

def set_price(self, price):
        self.price = price

def set_volume(self, volume):
        self.volume = volume



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


