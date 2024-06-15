class BMI:
     def __init__(self,sName,iAge,fHeight,fWeight):
            self.name=sName
            self.age=iAge
            self.height=fHeight
            self.weight=fWeight
     def getStatus(self):
        b=fWeight/(fHeight*fHeight)
        if b<18:
            return 'underweight'
        elif 25>b>=18:
            return 'ideal'
        elif 25<=b<27:
            return 'overweight'
        else:
            return 'obesity'
     def getBMI(self):
          b=fWeight/(fHeight*fHeight)
          return b

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

