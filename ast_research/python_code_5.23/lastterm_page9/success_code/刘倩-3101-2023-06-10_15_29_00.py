class Book:

    def __init__(self,shuming,shuhao,jiage):
        self.shuming = shuming
        self.shuhao = shuhao
        self.jiage = jiage

    def __del__(self):
        print(f"Book destroyes-{self.shuming},{self.shuhao},{self.jiage:.2f}")


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

