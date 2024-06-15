class Book:
    sName = None
    sNo = None
    fPrice = None
    def __del__(self):
        print("Book destroyed-%s,%s,%2f"%(sName,sNo,fPrice))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

