class bmi:
    def __init__(self,Name,Age,Height,Weight):
        self.name=sName
        self.age=float(iAge)
        self.height=float(fHeight)
        self.weight=float(fWeight)
    def getBMI(self,height,weight):
        return float(self.weight/(self.height)**2)
    def getStatus(self):
        if s.getBMI()<18:
            return underweight
        elif 18<=s.getBMI()<25:
            return ideal
        elif 25<=s.getBMI()<27:
            return overweight
        else:
            obesity

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

