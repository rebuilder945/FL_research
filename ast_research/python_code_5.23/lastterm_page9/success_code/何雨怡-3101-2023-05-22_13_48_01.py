class Book:
    def __init__(self,sName="N/A",sNo="N/A",fPrice="N/A"):
        self.sName=sName
        self.sNo=sNo
        self.fPrice=fPrice
        print("Book destroyed-",sName,sNo,"%.2f"%(fPrice))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

