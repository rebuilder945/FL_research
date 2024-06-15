class Book:
    def __init__(self,sName,sNo,fPrice):
        self.sName=sName
        self.sNo=sNo
        self.fPrice=fPrice
    def __del__(self):
        print("Book destroyed-{},{},{:.2f}".format(sName,sNo,fPrice))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

