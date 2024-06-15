class Book:
class Book:  
    def __init__(self, title, isbn, price):  
        self.title = title  
        self.isbn = isbn  
        self.price = price  
      
    def __del__(self):  
        print(f"Book destroyed - {self.title}, {self.isbn}, {round(self.price, 2)}")



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

