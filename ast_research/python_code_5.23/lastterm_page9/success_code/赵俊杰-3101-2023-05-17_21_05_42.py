class Book:
   def __init__(self,name,No,Price):
      self.name=name
      self.No=No
      self.Price=Price
   
      print("Book destroyed-%s,%s,%.2f"%(self.name,self.No,self.Price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

