class Book:
def _init_(self,sName="N/A",sNo="N/A",fPrice=0):
     self.str_name=sName 
     self.str_no=sNo
     self.float_price=float(fPrice) 
def _del_(self):
    print("Book destroyed-%s,%s,%.2f"%(self.str_name,self.str_no,self.float_price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

