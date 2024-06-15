class Book:
def _Book_(self,sName,sNo,fPrice):
    self.name=sName
    self.No=sNo
    self.price=float(fPrice)
    print("Book" sName,sNO,"{:.2f}".format(fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

