class BMI:
    def __init__(self,Name,Age,Height,Weight):
        self.name=Name
        self.age=Age
        self.height=Height
        self.weight=Weight
    def getBMI(self):
        b=self.weight/self.height**2
        return b
    def getStatus(self):
        if self.weight/self.height**2<18:
            return 'underweight '
        elif 18<=self.weight/self.height**2<25:
            return 'ideal'
        elif 25<=self.weight/self.height**2<27:
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

