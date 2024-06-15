class Book:
    def __init__(self,name,number,unit_cost):
        self.name=name
        self.number=number
        self.unit_cost=unit_cost
    def del__(self):
        print("Book destoryed-%s %s %.2f"%(self.name,self.number,self.unit_cost))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

