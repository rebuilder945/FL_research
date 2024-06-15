class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name = sName
        self.age = iAge
        self.height = fHeight
        self.weight = fWeight
    def getBMI(self):
        bmi = self.weight/self.height**2
        return bmi
    def getStatus(self):
        BMI = self.getBMI()
        if BMI<18:
            return "underweight"
        elif  18 <= BMI < 25 :
            return "ideal"
        elif 25 <= BMI < 27 :
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

