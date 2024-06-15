class Book:
    def __init__(self, Nam1, No1, Price1):
        print("Book destroyed-%s,%s,%.2f" %(Nam1, No1, Price1))
        self.Nam = Nam1
        self.No = No1
        self.Price = Price1


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

