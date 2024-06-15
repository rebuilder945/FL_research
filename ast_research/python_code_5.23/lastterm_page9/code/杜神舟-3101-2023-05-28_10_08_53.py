class Book:
    def __init__(self,sName='na',sNo='na',fPrice=0)
        self.sname=sName
        self.sno=sNo
        self.fpric=fPrice
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f" %(self.sname,self.sno,self.fpric))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

