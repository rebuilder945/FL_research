class Book:
    def __init__(self,sName='N/A',sNo='N/A',fPrice=0):
        self.str_Name=sName
        self.str_No=sNo
        self.float_Price=float(fPrice)
    def __del__(self):
        print('Book destroyed-%s,%s,%.2f'%(self.str_Name,self.str_No,self.float_Price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

