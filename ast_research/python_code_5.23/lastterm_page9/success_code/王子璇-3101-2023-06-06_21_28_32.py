class Book:
    def __int__(self,name,ids,price):
        self.name=name
        self.ids=ids
        self.price=price
    def __del__(self):
        print('Book destoryed-{},{},{:.2f}'.format(self.name,self.ids,self.price))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

