class BMI:
    def __init__(self,Name,Age,Height,Weight):
        self.sName=Name
        self.iAge=Age
        self.fHeight=Height
        self.fWeight=Weight
    def getBMI(self):
        return (self.fWeight/self.fHeight**2)
    def getStatus(self):
        if BMI<18:
            return "underweight"
        elif BMI>=18 and BMI<25:
            return "ideal"
        elif BMI>=25 and BMI<27:
            return "overweight"
        elif BMI>=27:
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

