class Book:
    def __del__(self,name="N/A",idNo="N/A",price="N/A"):
        self.sName = name
        self.sId = idNo
        self.fPrice = price
        s = "Book destroyed-%s,%s,%.2f"%(self.sName,self.sId,self.fPrice)
        retrun s


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

