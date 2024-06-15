class Book:
    def __init__(book,name,sno,fprice):
        book.sName=name
        book.sNo=sno
        book.fPrice=fprice
    def __del__(book):
        print("Book destroyed-%s,%s,%.2f"%(book.sName,book.sNo,book.fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

