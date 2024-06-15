class Book:
    def __init__(self,name,snumber,sprice):
        self.name=name
        self.snumber=snumber
        self.sprice=sprice
    def __del__(self):
        print("Book destroyed-{},{},{:.2f}".format(self.name,self.snumber,self.sprice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

