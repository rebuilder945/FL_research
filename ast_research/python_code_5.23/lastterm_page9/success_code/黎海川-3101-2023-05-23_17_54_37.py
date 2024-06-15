class Book:
    def __init__(self, sName, sNO, fPrice):
        self.sName = sName
        self.sNO = sNO
        self.fPrice = fPrice
    def sName(self):
        return self.sName
    def sNo(self):
        return self.sNO
    def fPrice(self):
        return self.fPrice
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f" %(self.sName,self.sNo,self.fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

