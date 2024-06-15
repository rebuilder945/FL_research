class Book:
 def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.sCode=sCode
        self.sName=sName
        self.priceYesterday=priceYesterday
        self.priceToday=priceToday
 def getCode(self):
        return sCode
 def getName(self):
        return sName
 def getPriceYesterday(self):
        return priceYesterday
 def getPriceToday(self):
        return priceToday
 def setPriceYesterday(self,a):
        priceYesterday=a
 def getChangePercent(self):
        return (priceYesterday-priceToday)/priceYesterday


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

