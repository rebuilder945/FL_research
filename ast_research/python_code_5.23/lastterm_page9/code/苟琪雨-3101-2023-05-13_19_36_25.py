class Book:
    def_init_(book,name="N/A",number="N/A",price="N/A"):
        book.sName=name
        book.sNo=number
        book.fPrice=price
        print("Book destroyed-%s,%s,%.2f"%(book.sName,book.sNo,book.fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

