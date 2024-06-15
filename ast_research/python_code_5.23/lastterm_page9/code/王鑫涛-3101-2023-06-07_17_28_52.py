class Book:
    def __init__(self='N/A',name='N/A',no,price=0):
        self.sName=name
        self.sNo=no
        self.fPrice=price
    def __del__(self):
        print('Book destroyed-%s,%s,%.2f'%(self.sName,self.sNo,self.fPrice)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

