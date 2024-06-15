class Book:
     def __init__(self,name,num,price):
        self.name=name
        self.num=num
        self.price=price
        print('Book destroyed-aaa,bbb,3.15')
    def _del_():
        print()


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

