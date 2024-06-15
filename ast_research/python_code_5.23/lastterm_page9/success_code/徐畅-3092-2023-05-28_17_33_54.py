class BMI:
    def __init__(self,name,age,c,d):
        self.name=name
        self.age=age
        self.c=c
        self.d=d
    def getBMI(self):
        a=self.d/(self.c)**2
        return a
    def getStatus(self):
        if BMI.getBMI(self)<18:
            return "underweight "
        elif BMI.getBMI(self)<25:
            return "ideal"
        elif BMI.getBMI(self)<27:
            return "overweight"
        else :
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

