class Book:
    def __init__(self,name=‘N/A’,no=‘N/A’,price=‘N/A’):
        self.sName=name
        self.sNo=no
        self.fPrice=float(‘%.2f’%price)
    def del(self):
        print(‘Book destoryed-‘,self.sName+’,’self.sNo+’,’self.fPrice)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

