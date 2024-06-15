class Book:
    def __init__(self,Name='',Nov='',Price=''):
        self.Name=Name
        self.Nov=Nov
        self.Price=Price
    def __del__(self):
        print('Book destroyed-'+self.Name+','+self.Nov+','+self.Price)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

