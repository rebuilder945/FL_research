class Book:
    def __init__(self,name,number,price):
        self.sName=name
        self.sNo=number
        self.fPrice=price
        ls=[]
        ls.append(self.sName)
        ls.append(self.sNo)
        ls.append(self.fPrice)
        print(",".join(str(x)for x in ls))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

