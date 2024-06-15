class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight,BMI="N/A"):
        self.name=sName
        self.age=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
        self.BMI=BMI
    def getBMI(self):
        self.BMI=self.fWeight/(self.fHeight**2)
        return self.BMI
    def getStatus(self):
        if self.BMI<18:
            return "underweight"
        elif self.BMI<25:
            return "ideal"
        elif self.BMI<27:
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

