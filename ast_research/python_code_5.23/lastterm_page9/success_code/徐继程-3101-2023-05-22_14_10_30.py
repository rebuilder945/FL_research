class Book:
    def __init__(self,name,no,price):
        self.sName=name
        self.sNo=no
        self.fPrice=price 
    # def sprint(self):
    #     print("Book destroyed-%s,%s,%.2f"%(self.sName,self.sNo,self.fPrice))
        print("Book destroyed-%s,%s,%.2f"%(self.sName,self.sNo,self.sPrice))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

