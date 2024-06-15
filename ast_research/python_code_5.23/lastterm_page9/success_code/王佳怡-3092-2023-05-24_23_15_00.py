class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def getBMI(self):
        return self.fWeight/self.fHeight**2
    def getStatus(self):
        if getBMI<18:
            return "underweight"
        elif getBMI<25:
            return "ideal"
        elif getBMI<27:
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

