class Book:
    def __init__(self,a,b1,c):
        self.a=a
        self.b1=b1
        self.c=c
    def __del__(self):
        print("Book destroyed-{},{},{%.2f}"(self.a,self.b1,self.c))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

