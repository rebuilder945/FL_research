class Book:
    def _init_(self,sName,sNo,fPrice):
        self.sName = sName
        self.sNo = sNo
        self.fPrice = fPrice
    def B(self):
        print ("Book destroyed-",(self.sName,self.sNo,self.fPrice))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

