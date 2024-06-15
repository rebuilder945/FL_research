class Book:
    def  __init__(self,a,b,c):
        self.name=a
        self.number=b
        self.price=c
    def __del__(self):
        print("Book destroyed- %s,%s,%.2f"%(self.name,self.number,self.price))
        
    
   



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

