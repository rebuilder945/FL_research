
class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.fHeight=float(fHeight)
        self.fWeight=float(fWeight)
    def name(self):
        return sName
    def age(self):
        return iAge
    def getBMI(self):
        return self.fWeight/(self.fHeight**2)
    def getStatus(self):
        value=self.fWeight/(self.fHeight**2)
        if value<18:
            return "underweight"
        elif value<25 and value>=18:
            return "ideal"
        elif value<27 and value>=25:
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

