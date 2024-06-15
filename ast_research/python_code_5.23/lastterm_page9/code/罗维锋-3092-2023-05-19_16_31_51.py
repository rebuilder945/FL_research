class BMI:
    def __init__(self,Name,iAge,fHeight,fWeight):
        self.name=Name
        self.age=iAge
        self.h=fHeight
        self.w=fWeight
    def getBMI(self):
        return self.w/（self.h）**2
    def getStatus(self):
        if self.w/（self.h）**2 < 18:
            return "underweight"
        elif self.w/（self.h）**2 < 25:
            return "ideal"
        elif self.w/（self.h）**2 <27:
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

