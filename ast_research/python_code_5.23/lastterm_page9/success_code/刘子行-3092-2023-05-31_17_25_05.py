class BMI:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def getBMI(self):
        self.aa=self.d/self.c**2
        return self.aa
    def getStatus(self):
        if self.aa<18:
            return 'underweight'
        elif self.aa>=18 and self.aa<25:
            return 'ideal'
        elif self.aa>=25 and self.aa<=27:
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

