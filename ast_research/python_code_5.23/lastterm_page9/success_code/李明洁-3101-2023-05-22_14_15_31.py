class Book:
    def _init_(self,sName,sNo,fPrice):
        self.sName = sName
        self.sNo = sNo
        self.fPrice = fPrice
    def _del_(self,b):
        print('Book destroyed-{},{},{:.2f}'.format(self.sName,self.sNo,self.fPrice))
        



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

