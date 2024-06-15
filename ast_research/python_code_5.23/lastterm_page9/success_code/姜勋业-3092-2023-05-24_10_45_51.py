class BMI:
     def __init__(self,name,age,height,weight):
            self.name=sName
            self.age=iAge
            self.height=fHeight
            self.weight=fWeight
     def getBMI(self):
           return self.weight/(self.height**2)
     def getStatus(self):
           k=getBMI()
           if k<18:
              return 'underweight'
           elif k>=18 and k<25:
              return 'ideal'
           elif k>=25 and k<27:
              return 'overweight'
           else:
              return 'obesity'

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

