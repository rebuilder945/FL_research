class Book:
def __init__(self,sName="N/A",sNo="N/A",fPrice="N/A"):
        Book.sName = sName
        Book.sNo = sNo
        Book.fPrice = fPrice
        print("Book destroyed-{},{},{}".format(sName,sNo,fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

