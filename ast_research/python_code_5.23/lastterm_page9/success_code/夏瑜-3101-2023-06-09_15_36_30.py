class Book:
    def __init__(self,sNme='N/A',sN="N/A",frice=0):
        self.sName=sNme
        self.sNo=so
        self.fPrice=frice
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f"%(self.sName,self.sNo,self.fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

