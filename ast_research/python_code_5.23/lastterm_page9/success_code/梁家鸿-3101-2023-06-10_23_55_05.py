class Book:
    def __init__(book,sName,sNo,fPrice):
        book.name = sName
        book.id = sNo
        book.price = fPrice
    def __del__(book):
        print("Book destroyed-"+book.name+','+book.id+','+str(book.price))
            


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

