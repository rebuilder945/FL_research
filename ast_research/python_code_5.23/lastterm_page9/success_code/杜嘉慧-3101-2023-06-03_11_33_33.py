class Book:
      def _init_(self,sname="N/A",sno="N/A",fprice="N/A"):
             self.name=sname
             self.no=sno
             self.price=fprice
      def __del__(self):
             print("Book destroyed-%s,%s,%.2f"%(self.name, self.no, self.price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

