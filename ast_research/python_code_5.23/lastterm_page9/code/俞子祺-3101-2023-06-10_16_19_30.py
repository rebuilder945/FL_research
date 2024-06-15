class Book:
def__init__(self,name,no,price):
    self.name=name
    self.no=no
    self.price=price
def__del__(self):
    print("Bool destroyed-"+self.name+","+self.no+","+self.price)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

