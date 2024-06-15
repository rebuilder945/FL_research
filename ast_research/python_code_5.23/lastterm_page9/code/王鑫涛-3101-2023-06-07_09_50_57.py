class Book:
    def __init__(self,name=‘N/A’,no=‘N/A’,price=‘N/A’):
        self.shame=name
        self.sno=no
        self.spruce=price
        


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

