class Book:
    def __init__(self,name="N/A",idNo="N/A",price="N/A"):
        self.sName = name
        self.sId = idNo
        self.fPrice = price
        t = "Book destroyed-%s,%s,%.2f"%(self.sName,self.sId,self.fPrice)
        return t


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

