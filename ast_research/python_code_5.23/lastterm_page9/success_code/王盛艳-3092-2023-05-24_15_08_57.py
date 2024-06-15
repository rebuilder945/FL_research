class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.height = fHeight
        self.weight = fWeight
        self.name = sName
        self.age = iAge
    def getStatus(self):
        a = fWeight/(fHeight*fHeight)
        if a < 18:
            return 'underweight'
        if 18 <= a < 25:
            return 'ideal'
        if 25 <= a < 27:
            return 'overweight'
        else:
            return 'obesity'
    def getBMI(self):
        a = fWeight/(fHeight*fHeight)
        return a

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

