class Book:
b=('Book destroyed-%.d,%.d,%.2f'%(sName,sNo,fPrice))
return b


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

