class Book:
    def __init__(self,sName,sNo,fPrice):
        self.name=sName
        self.no=sNo
        self.price=fPrice
    def __del__(self):
        return Book destroyed-self.name,self.no,self.price




        

  


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

