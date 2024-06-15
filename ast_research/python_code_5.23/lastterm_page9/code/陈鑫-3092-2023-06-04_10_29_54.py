class BMI:
    def __init__(self,a,b,c,d):
        self.name=a
        self.age=b
        self.c=c
        self.d=d
    def getBMI(self):
        y=0
        y+=self.d/self.c**2
        return y    
    def getStatus(self,getBMI(self)):
        if getBMI(self)<18:
            return 'underweight'
        elif 18<=getBMI(self)<25:
            return 'ideal'
        elif 25<=getBMI(self)<27:
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

