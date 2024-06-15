class Book:
class Book:    #创建book类
    def __init__(self,sName,sNo,fP):
        self.sName = sName
        self.sNo = sNo
        self.fPrice = fP
 
    def __del__(self):
        print('Book destroyed-{},{},{:.2f}'.format(self.sName,self.sNo,self.fPrice))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

