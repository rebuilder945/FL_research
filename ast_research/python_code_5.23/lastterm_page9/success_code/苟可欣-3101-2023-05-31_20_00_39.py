class Book:
    def Book (book,sName="N/A",sNo="N/A",fPrice="N/A"):
        self.name=sName
        self.no=sNo
        self.price=fPrice
    def __del__ (self):
        print("Book destroyed-",self.name,self.no,"%.2f"%(self.price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

