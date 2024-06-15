class Book:
    def __init__(self,name,no,price):
        self.name=name
        self.no=no
        self.price=price
        print("Book destroyed-%s,%s,%.s"%(self.name,self.no,self.price))
        


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

