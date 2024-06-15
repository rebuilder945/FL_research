class Book:
 def __init__(self,na="N/A",no="N/A",p="N/A"):
  self.sna=na
  self.sno=no
  self.sp=p
  
 def made(self):
  print("Book destroyed-%s,%s,%.2f"%(self.sna,self.sno,self.sp)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

