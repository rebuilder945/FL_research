class Book:
def__init__(self,sName,sNOo,fprice):
      self.sName=sName
      self.sNo=sNo
      self.fprice=fprice
def__del__(self):
      print("Book destroyed-%s,%s,%.2f"%self.sName,self.sNo,self.fprice)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

