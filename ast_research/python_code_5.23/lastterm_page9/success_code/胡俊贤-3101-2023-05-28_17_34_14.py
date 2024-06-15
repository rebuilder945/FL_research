class Book:
    def __init__(self,sName,sNo,fPrice):
        self.name=sName
        self.id=sNo
        self.price=fPrice
    def __del__(self):
        print("Book destroyed-",end='')
        print(self.name,end=',')
        print(self.id,end=',')
        print(self.price)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

