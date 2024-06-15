class Book:
    def _ _init_ _(self,name='N/A',number='N/A',price='N/A'):
        self.sName=name
        self.sNo=number
        self.fPrice=price
    def _ _del_ _(self):
        print("Book destoryed-%s,%s,%.2f"%(self.sName,self.sNo,self.fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

