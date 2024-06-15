class Book:
    def __init__(self,name,num,price):
        self.name=name
        self.num=num
        self.price=price
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f"%(self.name,self.num,self.price))
        


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

