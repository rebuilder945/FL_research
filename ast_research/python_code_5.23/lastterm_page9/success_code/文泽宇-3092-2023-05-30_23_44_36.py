class BMI:
    def __init__(self,mingzi,nian,H,W):
        self.name=mingzi
        self.age=nian
        self.h=H
        self.w=W
    def getBMI(self):
        bmi=(self.w)/((self.h)**2)
        return bmi
    def getStatus(self):
        bmi=(self.w)/((self.h)**2)
        if bmi <18:
            return 'underweight'
        elif bmi<25:
            return 'ideal'
        elif bmi<27:
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

