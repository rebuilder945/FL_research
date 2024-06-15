class Book:
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price

    def __del__(self):
        print(f"Book destroyed-{self.name},{self.number},{self.price:.2f}")



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

