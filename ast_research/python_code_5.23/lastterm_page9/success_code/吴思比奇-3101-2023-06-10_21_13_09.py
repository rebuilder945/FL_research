class Book:
    def _init_(self,x,y,z):
        self.str_x=x
        self.str_y=y
        self.float_z=float(z)
    def _del_(self):
        print('Book destroyed-%s,%s,%.2f'%(self.str_x,self.str_y,self.float_y))
        


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

