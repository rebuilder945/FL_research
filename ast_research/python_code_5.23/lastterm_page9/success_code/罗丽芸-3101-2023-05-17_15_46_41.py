class Book:
      def __init__(self,sName,iAge,fHeight,fWeight):
            self.name=sName
            self.age=iAge
            self.height=fHeight
            self.weight=fWeight
      def getBMI(self):
            return self.weight/(self.height**2)
      def getStatus(self):
            a=self.weight/(self.height**2)
            if a<18:
                 return "underweight"
            elif a>=18 and a<25:
                 return "ideal"
            elif a>=25 and a<27:
                 return "overweight"
            else:
                 return "obesity"



sName = input()  #Input Book Name
sNo = input() #Input Book Number
fPrice = float(input())   #Input Book Price
b = Book(sName,sNo,fPrice)
b = None   #__del__ method of object b been triggered 

