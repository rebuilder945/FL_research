class Book:
class Number():
    def __init__(self, n1, n2):
        self.__n1 = n1
        self.__n2 = n2
    def addition(self):
        m1 = self.__n1 + self.__n2
        print('%d+%d=%d' % (self.__n1,self.__n2,m1))
    def subtration(self):
        m2 = self.__n1 - self.__n2
        print('%d-%d=%d'  %  (self.__n1,self.__n2,m2))
n1, n2, op = input().split(",")
mm = Number(int(n1), int(n2))
if op == 'add':
    mm.addition()
elif op == 'sub':
    mm.subtration()
else:
    print("error!")



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

