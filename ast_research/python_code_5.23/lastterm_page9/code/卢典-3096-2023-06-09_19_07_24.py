#class Stock
 def __init__(self, code: str, name: str, yesterday_price: float, today_price: float):
        self.__code = code
        self.__name = name
        self.__yesterday_price = yesterday_price
        self.__today_price = today_price

    def get_name(self) -> str:
        return self.__name

    def get_code(self) -> str:
        return self.__code

    def get_yesterday_price(self) -> float:
        return self.__yesterday_price

    def set_yesterday_price(self, price: float):
        self.__yesterday_price = price

    def get_today_price(self) -> float:
        return self.__today_price

    def set_today_price(self, price: float):
        self.__today_price = price

    def get_change_percent(self) -> str:
        change_percent = (self.__today_price - self.__yesterday_price) / self.__yesterday_price * 100
        return f"{change_percent:.2f}%"


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


