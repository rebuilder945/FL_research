class BMI:
    def __init__(self,name,age,height,weight):
         self.name=name
         self.age=age
         self.height=height
         self.weight=weight
    def getBMI(self):
          a=self.weight/self.height*self.height
          return a
    def getStatus(self):
          a=self.weight/self.height*self.height
          if a<18:
                 return "underweight"
          elif 18<=a<=25:
                 return "ideal"
          elif 25<=a<=27:
                 return "overweight"
           else:
                return "obesity"

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

