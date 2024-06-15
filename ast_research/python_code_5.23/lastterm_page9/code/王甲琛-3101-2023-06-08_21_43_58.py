class Book:
class  Book:
    def __init__(s,a,b,c):
        print("Book destroyed",end="")
        print(a,b,c)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

