class Book:
    def __init__(self,sName,sNo,fPrince):
        self.sName=sName
        self.sNo=sNo
        self.fPrice='%.2f'%fPrice
    def __dell__(self):
        print(Book destroyed-sName,sNo,fPrice)



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

