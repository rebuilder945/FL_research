class Book:
    def __init__(self, Name, No,fPrice):
        self.sName=sName
        self.sNo=sNo
        self.fPrice=fPrice
    def __del__(self):
        print(f"Book destroyed-{self.sName},{self.sNo},{self.fPrice:.2f}")


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

