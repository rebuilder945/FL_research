class Book:
def _init_(self,sName,sNo,fPrice):
    self.name=sName
    self.No=sNo
    self.price=float(fPrice)
def _del_(self):
    print("Book destroyed-{},{},{:.2f}".format(self.name,self.No,self.price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

