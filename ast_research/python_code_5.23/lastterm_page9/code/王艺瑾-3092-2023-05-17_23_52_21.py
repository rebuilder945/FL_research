class BMI
    def __init__(self,sName,iAge,fHeight,fWeight):
        bmi.name=sName
        bmi.age=iAge
        bmi.height=fHeight
        bmi.weight=fWeight
    def getBMI(self):
        return bmi.weight/bmi.height**2
    def getStatus(self):
        if bmi.getBMI()<18:
            return "underweight"
        elif bmi.getBMI() in range(18,25):
            return "ideal"
        elif bmi.getBMI() in range(25,27):
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

