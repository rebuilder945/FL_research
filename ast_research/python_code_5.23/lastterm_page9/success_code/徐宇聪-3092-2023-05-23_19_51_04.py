class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name = sName
        self.age = iAge
        self.height = fHeight
        self.weight = fWeight

    def getBMI(self):
        self.BMI = self.weight/(self.height**2) 
        return self.BMI

    def getStatus(self):
        if  self.BMI < 18:
            return "underweight"
        elif  18 <= self.BMI < 25:
            return "ideal"
        elif  25 <= self.BMI < 27:
            return "overweight"
        elif  self.BMI >= 27:
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

