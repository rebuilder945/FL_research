class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=int(age)
        self.height=float(height)
        self.weight=float(weight)
    def getBMI(self):
        return self.weight/(self.height*self.height)
    def getStatus(self):
        if self.getBMI()<18:
            return "underweight"
        elif self.getBMI()>=18 and self.getBMI()<25:
            return "ideal"
        elif self.getBMI()>=25 and self.getBMI()<27:
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

