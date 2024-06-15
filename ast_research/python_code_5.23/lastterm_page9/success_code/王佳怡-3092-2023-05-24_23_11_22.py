class BIM:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.sName=sName
        self.iAge=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def getBIM(self):
        return self.fHeight/self.fWeight**2
    def getStatus(self):
        if getBIM<18:
            return "underweight"
        elif getBIM<25:
            return "ideal"
        elif getBIM<27:
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

