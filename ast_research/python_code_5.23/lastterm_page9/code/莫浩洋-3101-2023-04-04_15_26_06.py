class Book:
 def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.sCode=sCode
        self.sName=sName
        self.priceYesterday=priceYesterday
        self.priceToday=priceToday
 def getCode():
        return sCode
  def getName():
        return sName
  def getPriceYesterday():
        return priceYesterday
  def getPriceToday():
        return priceToday
  def setPriceYesterday(self,a):
        priceYesterday=a
  def getChangePercent():
        return (priceYesterday-priceToday)/priceYesterday


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

