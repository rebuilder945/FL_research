class Book:
    def __init__(self, name, book_no, price):
        self.name = name
        self.book_no = book_no
        self.price = price
    
    def __del__(self):
        print(f"Book destroyed-{self.name},{self.book_no},{format(self.price, '.2f')}")


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

