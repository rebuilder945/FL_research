class BMI:
    def __init__(self,name,age,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def getBMI(self):
        return self.fWeight/(self.fHeight**2)
    def getStatus(self):
        d=self.fWeight/(self.fHeight**2)
        if d<18:
            return 'underweight'
        elif d<25:
            return 'ideal'
        elif d<27:
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

