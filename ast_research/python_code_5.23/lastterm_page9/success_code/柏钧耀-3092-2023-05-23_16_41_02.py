class BMI:
    def __init__(self,a,b,c,d):
        self.name=a
        self.age=b
        self.c=c
        self.d=d
    def name(self):
        return str(self.a)
    def age(self):
        return str(self.b)
    def getBMI(self):
        return self.d/self.c**2
    def getStatus(self):
        bmi=float(self.getBMI())
        if bmi>=27:
            return "obesity"
        elif bmi>=25 and bmi<27:
            return "overweight"
        elif bmi >=18 and bmi < 25:
            return "ideal"
        else:
            return "underweight"


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

