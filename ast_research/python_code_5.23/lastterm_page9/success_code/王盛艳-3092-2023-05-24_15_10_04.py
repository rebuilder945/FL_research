class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.height = fHeight
        self.weight = fWeight
        self.name = sName
        self.age = iAge
    def getStatus(self):
        BMI = fWeight/(fHeight*fHeight)
        if BMI < 18:
            return 'underweight'
        if 18 <= BMI < 25:
            return 'ideal'
        if 25 <= BMI < 27:
            return 'overweight'
        else:
            return 'obesity'
    def getBMI(self):
        BMI = fWeight/(fHeight*fHeight)
        return BMI

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

