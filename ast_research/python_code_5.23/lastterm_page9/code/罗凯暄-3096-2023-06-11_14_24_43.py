#class Stock
    def __init__(self, code, name, yesterday_price, today_price):
        self.__code = code
        self.__name = name
        self.__yesterday_price = yesterday_price
        self.__today_price = today_price

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code

    def get_yesterday_price(self):
        return self.__yesterday_price

    def set_yesterday_price(self, price):
        self.__yesterday_price = price

    def get_today_price(self):
        return self.__today_price

    def set_today_price(self, price):
        self.__today_price = price

    def get_change_percent(self):
        return '{:.2%}'.format((self.__today_price - self.__yesterday_price) / self.__yesterday_price)

if __name__ == '__main__':
    stock = Stock('601318', 'Chinese PINAN', 63.21, 64.39)
    print('Code:{}'.format(stock.get_code()))
    print('Name:{}'.format(stock.get_name()))
    print('Price/Yesterday:{}'.format(stock.get_yesterday_price()))
    print('Price/Today:{}'.format(stock.get_today_price()))
    stock.set_yesterday_price(50.25)
    print('Edit Price/Yesterday To:{}'.format(stock.get_yesterday_price()))
    print('Price Change Percentage:{}'.format(stock.get_change_percent()))

```


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


