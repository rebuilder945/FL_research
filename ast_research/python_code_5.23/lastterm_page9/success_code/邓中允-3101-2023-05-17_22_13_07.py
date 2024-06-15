class Book:
    def __init__(self,name,shuhao,danjia):
        self.name=name
        self.shuhao=shuhao
        self.danjia=danjia
    def __del__(self):
        print("Book destroyed-%s,%s,%.2f"%(self.name,self.shuhao,self.danjia))


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

