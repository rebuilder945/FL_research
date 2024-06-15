class Book:
    def __init__(self,sname='N/A',sid='N/A',sprice=-1):
        self.name=sname
        self.id=sid
        self.price=sprice
        print('Book destroyed-'+self.name+','+self.id+','+'%.2f'%(self.price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

