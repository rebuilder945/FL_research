class Book:
    def __init__(self,name,No,price):
        self.sName=name
        self.sNo=No
        self.fPrice=price
    def name(self):
        return self.sName
    def number(self):
        return self.sNo
    def price(self):
        return self.fPrice
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f" %(self.sName,self.sNo,self.fPrice))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

