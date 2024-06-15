#class Stock
 Class Stock:
       "Stock Information Class"
        def __init__(self,c,n,y,t):
              self.c=c
              self.n=n
              self.y=y
              self.t=t
         def getCode(self):
               return self.c
         def getName(self):
               return self.n
         def getPriceYesterday(self):
               return self.y
         def getPriceToday(self):
               return self.t
          def setPriceYesterday(self,x):
                self.y=x
          def setPriceToday(self,x):
                self.t=x
          def getChangePercent(self):
                return (self.t-self.y)/self.y



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


