class Book:
    def __init__(self,name,num,price):
        self.Name = name
        self.Num = num
        self.Price = price
    def _del_(self):
        print('Book destroyed-'+self.Name+','+self.Num+','+'%.2f'%self.Price)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

