class Book:
    def __init__(self, sname , sno, fprice ):
        self.name = sname
        self.no = sno
        self.price = fprice
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f"%(sname, sno, fprice))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

