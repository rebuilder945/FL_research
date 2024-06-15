class Book:
    def _init_(self,sname,sno,fprice):
        self.sname=sname
        self.sno=sno
        self.fprice=fprice
        print("Book destroyed-%s,%s,%.2f"%(self.sname,self.sno,self.fprice))
    def _del_(self):
        
        


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

