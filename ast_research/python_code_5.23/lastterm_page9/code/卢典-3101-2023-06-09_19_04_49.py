class Book:
def __init__(self, book_name: str, book_id: str, price: float):
        self.book_name = sName
        self.book_id = sNo
        self.price = round(fprice, 2)

    def __del__(self):
        print(f"Book destroyed-{self.book_name},{self.book_id},{self.price}")


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

