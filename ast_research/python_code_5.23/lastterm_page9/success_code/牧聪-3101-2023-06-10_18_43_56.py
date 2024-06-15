class Book:
    def __init__(self,Name,No,Price):
        self.Name=sName
        self.No=sNo
        self.Frice=fPrice
    def __del__(self):
        print(f"Book .destroyed-{self.Name},{self.No},{self.Frice}")   


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

