class Book:
    def __init__(self,shuming,shuhao,danjia):
        self.shuming=sName 
        self.shuhao=sNo
        self.danjia=fPrice
    def __del__(self):
        print("Book","destroyed-"+self.shuming+","+self.shuhao+","+"%f.2"%self.price)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

