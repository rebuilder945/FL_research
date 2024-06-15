class Book:
    "user defined class:Book"
    def __init__(self,name,number,price):
       self.sName=name
       self.sNO=number
       self.fprice=price
    def __del__(self):
        print("Book destroyed-"+self.sName+","+self.sNO+",","%.2f"%(self.fprice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

