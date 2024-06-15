class Book:
def __init__(self,sName,sNo,fPrice):
        self.str_name=sName
        self.str_no=sNo
        self.float_price=float(fPrice)
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f" %(self.str_name,self.str_no,self.float_price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

