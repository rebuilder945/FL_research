class Book:
    def __init__(Book,Name,No,Price):
        Book.Name=sName
        Book.No=sNo
        Book.Price=fPrice  
        Book.destroyed=print("Book destoryed-%s,%s,%.2f"%(Book.Name,Book.No,Book.Price))



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

