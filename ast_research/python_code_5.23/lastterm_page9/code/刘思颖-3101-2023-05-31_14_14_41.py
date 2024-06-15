class Book:
def __init__(self,a,b,c,d):
            self.a=a
            self.b=b
            self.c=c
            self.d=d
def getCode(self):
            return self.a 
def getName(self):
            return self.b 
def getPriceYesterday(self):
            return self.c
def getPriceToday(self):
            return self.d
def setPriceYesterday(self,ee):
            self.vb=(self.d-ee)/ee
def getChangePercent(self):
            return self.vb



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

