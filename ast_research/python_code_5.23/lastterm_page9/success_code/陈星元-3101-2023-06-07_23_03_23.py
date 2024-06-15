class Book:
    def __init__(self,iname,iNo,iprice):
        self.iname=iname
        self.iNo=iNo
        self.iprice=iprice
    def __del__(self):
        print("Book destroyed-{},{},{:.2f}".format(self.iname,self.iNo,self.iprice))
        
    
   



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

