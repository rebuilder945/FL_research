#class Stock
class Stock:
    """
    Stock Information Class
    """

    def __init__(self, code: str, name: str, price_yesterday: float, price_today: float):
        """
        构造方法，初始化股票代码、股票名称、前一天股票价格、当天股票价格等属性。
        :param code: 股票代码
        :param name: 股票名称
        :param price_yesterday: 前一天股票价格
        :param price_today: 当天股票价格
        """
        self.__code = code
        self.__name = name
        self.__price_yesterday = price_yesterday
        self.__price_today = price_today

    def getName(self) :
       
        return self.__name

    def getCode(self) :
       
        return self.__code

    def getPriceYesterday(self) :
        
        return self.__price_yesterday

    def setPriceYesterday(self, price_yesterday: float):
      
        self.__price_yesterday = price_yesterday

    def getPriceToday(self):
 
        return self.__price_today

    def setPriceToday(self, price_today: float):
    
        self.__price_today = price_today

    def getChangePercent(self) -> float:
    
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


