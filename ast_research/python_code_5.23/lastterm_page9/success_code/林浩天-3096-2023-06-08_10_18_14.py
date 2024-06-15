#class Stock
class Stock:
    """
    Stock Information Class
    """

    def __init__(self, code, name, price_yesterday, price_today):
        """
        Constructor for Stock class
        :param code: str, stock code
        :param name: str, stock name
        :param price_yesterday: float, yesterday's stock price
        :param price_today: float, today's stock price
        """
        self.__code = code
        self.__name = name
        self.__price_yesterday = price_yesterday
        self.__price_today = price_today

    def getCode(self):
        """
        Getter method for stock code
        :return: str, stock code
        """
        return self.__code

    def getName(self):
        """
        Getter method for stock name
        :return: str, stock name
        """
        return self.__name

    def getPriceYesterday(self):
        """
        Getter method for yesterday's stock price
        :return: float, yesterday's stock price
        """
        return self.__price_yesterday

    def setPriceYesterday(self, price_yesterday):
        """
        Setter method for yesterday's stock price
        :param price_yesterday: float, yesterday's stock price
        """
        self.__price_yesterday = price_yesterday

    def getPriceToday(self):
        """
        Getter method for today's stock price
        :return: float, today's stock price
        """
        return self.__price_today

    def setPriceToday(self, price_today):
        """
        Setter method for today's stock price
        :param price_today: float, today's stock price
        """
        self.__price_today = price_today

    def getChangePercent(self):
        """
        Calculates change percentage in stock price from yesterday to today
        :return: float, change percentage in stock price
        """
        return (self.__price_today - self.__price_yesterday) / self.__price_yesterday



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


