class Book:
    def __init__(self='N/A',name='N/A',no,price=0):
        self.str_Name=name
        self.str_No=no
        self.str_Price=price
    def __del__(self):
        print('Book destroyed-%s,%s,%.2f'%(self.Name,self.No,self.Price)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

