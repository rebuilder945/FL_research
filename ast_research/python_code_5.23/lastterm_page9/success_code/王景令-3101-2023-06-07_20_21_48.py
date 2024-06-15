class Book:
    def _init_(self,a,b,c):
        self.sName = a
        self.sNo = b
        self.fPrice = c


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

