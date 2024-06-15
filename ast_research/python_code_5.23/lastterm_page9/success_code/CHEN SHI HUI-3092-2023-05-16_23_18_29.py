class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.Height=fHeight
        self.Weight=fWeight

    def getBMI(self):
        return self.Weight/(self.Height**2)

    def getStatus(self):
        s=self.getBMI()
        if s<18:
            return "underweight"
        elif 18<=s<25:
            return "ideal"
        elif 25<=s<27:
            return "overweight"
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

