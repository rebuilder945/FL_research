class Book:
    def __init__(self,Name,No,Price):
        self.Name = Name
        self.No = No
        self.Price = Price
        print("Book destroyed-{},{},{:.2f}".format(self.Name,self.No,self.Price))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

