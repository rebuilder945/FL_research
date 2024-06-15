class Book:
  def __init__(self,a,b,c):
    self.name=a
    self.no=b
    self.price='%.2f'%c

  
  def _del_(self):
    info=self.name+','+self.no+','+self.price
    print('Book destroyed-'+info)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

