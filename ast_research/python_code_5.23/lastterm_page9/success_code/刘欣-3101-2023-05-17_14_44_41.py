class Book:
    def __init__(self,sName,sNo,fPrice):
        self.name=sName
        self.number=sNo
        self.price=fPrice
        print("Book %s,%s,%.2f"%(self.name,self.number,self.price))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

