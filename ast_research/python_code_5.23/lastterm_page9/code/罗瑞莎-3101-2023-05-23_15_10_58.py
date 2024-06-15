class Book:
    def __init__(self,name,id,price):
        self.sName = name
        self.sNo = id
        self.fPrice = price

    def del(self):
        print("Book destroyed-%s,%s,%.2f"%(self.sName,self.sNo,self.fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

