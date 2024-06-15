class Book:
    def __init__(self,sName='N/A',sNo='N/A',fPrice='N/A'):
        self.Name = sName
        self.No = sNo
        self.Price = fPrice
        words = 'Book destroyed-%s,%s,%.2f'%(self.Name,self.No,self.Price)
        print(words)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

