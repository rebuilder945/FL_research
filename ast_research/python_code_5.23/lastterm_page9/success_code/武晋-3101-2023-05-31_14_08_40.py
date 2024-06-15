class Book:
    def __init__(self,sName,sNo,fprice):
        self.sName=sName
        self.sNo=sNo
        self.fprice=fprice
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f"%self.sName,self.sNo,self.fprice)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

