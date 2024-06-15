class BMI:
 def_init_(self, name,age,height,weight):
  self.name=name
  self.age=age
  self.height = height
  self.weight=weight
def getBMI(self):
 return self.weight / (self.height **2)
def getStatus(self):
 value = self.weight /(self.height ** 2)
 if value < 18:
  return "underweight"
 elif value < 25:
  return "ideal"
 elif value < 27:
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

