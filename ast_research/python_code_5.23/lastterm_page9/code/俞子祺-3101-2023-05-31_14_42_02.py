class Book:
    def__init__(sName,sNo,fPrice):
        self.name=name
        self.number=number
        self.price=price
    def__del__(self):
        print('Book destroyed-{},{},{:.2f}'.format(self.name,self.number,self.price))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

