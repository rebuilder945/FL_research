class Book:
    def __init__(self,Name,No,Price):
        self.Name=sName
        self.No=sNo
        self.Price=fPrice
    def __del__(self):
        print('Book destroyed-%s,%s,%.2f'%((self.Name),(self.No),(self.Price)))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

