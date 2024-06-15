class Book:
class  Book:
    def __init__(self,sName,sNo,fp):
        self.name=sName
        self.sNo=sNo
        self.fPrice=fp
    def zhixin(self):
        print('Book destroyed-{},{},{:.2f}.format(sName,sNo,fp)')
        


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

