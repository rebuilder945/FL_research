class Book:
    def __init__(self,a = 'name',b = 'sno',c = 'fprice'):
        self.sName = a
        self.sNo = b
        self.fPrice = c


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

