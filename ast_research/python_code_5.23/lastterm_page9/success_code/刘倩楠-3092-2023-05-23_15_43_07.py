class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=str(sName)
        self.age=int(iAge)
        self.height=float(fHeight)
        self.weight=float(fWeight)
    def getBMI(self):
        return self.weight/pow(self.height,2)
    def getStatus(self):
        value=self.weight/pow(self.height,2)
        if value<18:
            return "underweight"
        elif 18<=value<25:
            return "ideal"
        elif 25<=value<27:
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

