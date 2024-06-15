class Book:
    def __init__(self,name,no,price):
        self.name=name
        self.no=no
        self.price=price

    def __del__(self):
        print(f"Book destroyed-{self.name},{self.no},{self.price:.2f}")


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

