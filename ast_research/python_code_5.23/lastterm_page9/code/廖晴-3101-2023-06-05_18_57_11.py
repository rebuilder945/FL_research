class Book:
    def __init__(self,sName,sNo,fPrice):
        self.sName=sName
        self.sNo=sNo
        self.fPrice=“%.{}f”.format(2)%fPrice
        print("Book destoryed-",sName,sep="",end="")
        print("",sNo,fPrice,sep=",")



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

