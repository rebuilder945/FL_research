class Book:
    def __init__(self,name,No,price):
        self.name = name
        self.No = No
        self.price = price
    def __del__(self) -> None:
       print('Book destroyed-{},{},{:.2f}'.format(self.name,self.No,self.price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

