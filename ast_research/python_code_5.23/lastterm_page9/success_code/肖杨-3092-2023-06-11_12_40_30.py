class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def getBMI(self):
        self.h=self.fWeight/self.fHeight**2
        return self.fWeight/self.fHeight**2
    def getStatus(self):
        if self.h<18:
            return 'underweight'
        if 18<=self.h<25:
            return 'ideal'
        if 25<=self.h<27:
            return 'overweight'
        if 27<=self.h:
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

