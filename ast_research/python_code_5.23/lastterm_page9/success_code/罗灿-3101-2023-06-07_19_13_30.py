class Book:
    def __init__(self,name="N/A",id="N/A",price="N/A"):
        self.sName=name
        self.sID=id
        self.sPrice=price

    def __del__(self):
        print("Book destroyed-%s,%s,%.2f"%(self.sName,self.sID,self.sPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

