class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.sName=sName
        self.iAge=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def getBMI(self):
        a=self.fWeight/(self.fHeight)**2
        return a
    def getStatus(self):
        a=self.fWeight/(self.fHeight)**2
        if a<18:
            return 'underweight'
        elif 18<=a<25:
            return 'ideal'
        elif 25<=a<27:
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

