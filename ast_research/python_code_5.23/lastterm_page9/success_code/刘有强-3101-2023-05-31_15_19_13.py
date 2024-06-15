class Book:
    def __init__(self,no,idNo,name):
        self.Bookname= no
        self.bookno= idNo
        self.Bookprice= name
    
    def __del__(self):
        print("Book destroyed-%s,%s,%0.2f"%(self.Bookname,self.bookno,self.Bookprice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

