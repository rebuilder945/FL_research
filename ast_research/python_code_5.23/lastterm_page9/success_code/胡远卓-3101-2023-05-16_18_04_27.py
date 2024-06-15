class Book:
    def __init__(self,a,b,c):
        self.Name=a
        self.sNo=b
        self.fPrice=c
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f"%(self.Name,self.sNo,self.fPrice))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

