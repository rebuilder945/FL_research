class Book:
def __del__(self):
    print("Book destroyed-", self.name, ",", self.isbn, ",", self.price)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

