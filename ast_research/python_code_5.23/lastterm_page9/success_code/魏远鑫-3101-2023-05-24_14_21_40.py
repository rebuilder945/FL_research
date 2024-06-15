class Book:
    def __init__(self,shuming,shuhao,danjia):
        self.shuming=sName 
        self.shuhao=sNo
        self.danjia=fPrice
    def speak(self):
        print("Book","destroyed-"+self.shuming+","+self.shuhao+","+"%.2f"%self.danjia)


sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

