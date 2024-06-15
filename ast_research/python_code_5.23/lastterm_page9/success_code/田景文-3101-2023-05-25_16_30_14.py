class Book:
    def __init__(self,sName,sNo,fPrice):
        self.sName: str = sName
        self.sNo: str = sNo
        self.fPrice: float = fPrice
    def __del__(self):
        print(f"Book destroyed-{sName},{sNo},{fPrice:.2f}")


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

