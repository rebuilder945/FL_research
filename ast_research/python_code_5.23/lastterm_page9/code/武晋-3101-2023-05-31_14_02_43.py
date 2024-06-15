class Book:
def_imit_(self,sName,sNOo,fprice):
      self.sName=sName
      self.sNo=sNo
      self.fprice=fprice
def_del_(self):
      print("Book destroyed-%s,%s,%.2f"%self.sName,self.sNo,self.fprice)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

