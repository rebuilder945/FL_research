class Book:
    def __init__(self,name,nNo,Price):
        self.name=str(sName)
        self.nNo = str(sNo)
        self.Price =float(fPrice)
    def Book(self):
        print("Book destroyed- %s,%s,%.2f"%(self.name,self.nNo,self.Price)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

