class Book:
    def __init__(self,a,b,c):
        self.name=a
        self.hao=b
        self.jiage=c
        s='Book destroyed-{},{},{}'.format(self.name,self.hao,self.jiage)
        print(s)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

