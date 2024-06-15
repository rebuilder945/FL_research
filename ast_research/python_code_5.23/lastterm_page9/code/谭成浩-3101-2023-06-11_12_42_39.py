class Book:
def __init__(self,name,no,price):
    self.Name=name
    self.No=no
    self.Price=price

def __del__(self):
    print('Book destroyed-{},{},{:.2f}'.format(self.Name,self.No,self.Price))
    


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

