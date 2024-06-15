class Book:
    def __init__(s,a,b,c):
        s.a=a
        s.b=b
        s.c=c
    def __del__(s):
        print("Book destroyed-%d,%d,%d"(s.a,s.b,s.c))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

