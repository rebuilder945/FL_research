class BMI:
    def __init__(self,a,b,c,d):
        self.name=a
        self.age=b
        self.c=c
        self.d=d
    def getBMI(self):
        y=self.d/self.c**2
        return y    
    def getStatus(self):
        x=self.d/self.c**2
        if x<18:
            return 'underweight'
        elif 18<=x<25:
            return 'ideal'
        elif 25<=x<27:
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

