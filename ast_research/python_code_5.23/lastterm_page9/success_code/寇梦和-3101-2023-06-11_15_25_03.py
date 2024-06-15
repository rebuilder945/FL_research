class Book:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __del__(self):
        print(f"Book destroyed-{self.a},{self.b},{self.c:.2f}")



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

