class BMI:
    def __init__(self,a,b,c,d):
        self.name=a
        self.age=b
        self.height=c
        self.weight=d
        self.m=0
        
    def name(self):
        return self.name
    def age(self):
        return self.age
    def getBMI(self):
        self.m+=self.weight/self.height**2
        return self.m
    def getStatus(self):
        if self.m<18:
            return "underweight"
        elif self.m<25:
            return "ideal"
        elif self.m<27:
            return "overweight"
        else:
            return "obesity"

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

