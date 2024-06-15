class Book:
    def__init__(book,sName,sNo,fPrice):
        book.sName=sName
        book.sNo=sNo
        book.fPrice=fPrice
    def__del__(self):
        print("Book destroyed-%s,%s,%.2f"%(book.sName,book.sNo,book.fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

