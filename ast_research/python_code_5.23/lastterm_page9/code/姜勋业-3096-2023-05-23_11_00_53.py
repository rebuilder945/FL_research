#class Stock
class Stock:
     def __init__(self,sCode,sName,priceYesterday,priceToday):
             self.sCode=sCode
             self.sName=sName
             self.priceYesterday=priceYesterday
             self.priceToday=priceToday
      def  get__Code(self):
              return self.sCode
      def  get__Name(self):
              return self.sName
      def get__PriceYesterday(self):
             return self.priceYesterday
      def get__PriceToday(self):
             return self.priceToday
      def set__PriceYesterday(self,x):
             self.priceToday=x
      def get__ChangePercent(self):
             return (self.priceToday-self.priceYesterday)/self.priceYesterday


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


