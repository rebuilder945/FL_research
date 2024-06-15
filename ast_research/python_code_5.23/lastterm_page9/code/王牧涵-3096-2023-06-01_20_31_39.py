#class Stock
    # 构造方法
    def __init__(self, code, name, priceYesterday, priceToday):
        self.__code = code # 股票代码
        self.__name = name # 股票名称
        self.__priceYesterday = priceYesterday # 前一天股票价格
        self.__priceToday = priceToday # 当天股票价格

    # 股票代码的get方法
    @property
    def code(self):
        return self.__code

    # 股票名称的get方法
    @property
    def name(self):
        return self.__name

    # 前一天股票价格的get和set方法
    @property
    def priceYesterday(self):
        return self.__priceYesterday

    @priceYesterday.setter
    def priceYesterday(self, value):
        self.__priceYesterday = value

    # 当天股票价格的get和set方法
    @property
    def priceToday(self):
        return self.__priceToday

    @priceToday.setter
    def priceToday(self, value):
        self.__priceToday = value

    # 返回前日收市价至当前价格的变化百分比的方法
    def getChangePercent(self):
        return (self.__priceToday - self.__priceYesterday) / self.__priceYesterday


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


