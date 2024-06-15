class Book:
    def __init__(self,Book Name,Book Number,Book price):
        self.Book Name = sName
        self.Book Number = sNo
        self.Book Price = fPrice


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

