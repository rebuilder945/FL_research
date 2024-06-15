class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.sName=sName
        self.iAge=iAge
        self.fHeight=fHeight
        self.fWeight =fWeight 
    def getBMI(self):
        c = fWeight/fHeight**2
        return c
    def getStatus(self):
        d = fWeight/fHeight**2
        if d<18:
            return "underweight"
        if 18<=d<25:
            return "ideal"
        if 25<=d<27:
            return "overweight"
        if 27<=d:
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

