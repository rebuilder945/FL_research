class BMI:
    def __init__(self,sName,iAge,fWeight,fHeight):
        self.name=sName
        self.age=iAge
        self.weight=fWeight
        self.height=fHeight
    def getBMI(self):
        b=fWeight/fHeight**2
        return b
    def getStatus(self):
        if b<18:
            return "underweight"
        elif b>=18 and b<25:
            return "ideal"
        elif b>=25 and b<27:
            return "overweight"
        elif b>=27:
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

