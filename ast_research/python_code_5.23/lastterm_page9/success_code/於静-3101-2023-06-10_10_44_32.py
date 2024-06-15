class Book:
    def hanshu1(self,name,no,price):
        self.sName=name
        self.sNo=no
        self.fPrice=price
    def hanshu2(self):
        print("Book destroyed-%s,%s,%.2f"%(self.sName,self,self.sNo,self.fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

