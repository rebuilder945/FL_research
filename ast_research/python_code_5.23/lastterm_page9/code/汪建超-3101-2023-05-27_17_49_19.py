class Book:
 def  __init__(self,name="N/A",number="N/A",price = "N/A"):
    self.sName = name
    self.sNo = number
    self.fPrice = price
    print("Book destroyed-",self.sName','self.sNo',%.2f' % self.fPrice)



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

