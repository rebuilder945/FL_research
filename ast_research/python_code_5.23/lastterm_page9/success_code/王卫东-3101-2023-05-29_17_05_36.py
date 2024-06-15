class Book:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print('Book&#160;destroyed-aaa,bbb,3.15')
    def __del__():
        print('Book&#160;destroyed-aaa,bbb,3.15')


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

