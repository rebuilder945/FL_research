class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def getBMI(self):
        return self.fWeight/self.fHeight**2
    def getStatus(self):
        n=self.fWeight/self.fHeight**2
        if n<18:
            return "underweight"
        elif 18<=n<25:
            return " ideal"
        elif 25<=n<27:
            return "overweight"
        elif 27<=n:
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

