class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        return self.weight/(self.height**2)
    def getStatus(self):
        a=self.weight/(self.height**2)
        if a<18:
            return "underweight"
        elif a>=18 and a<25:
            return "ideal"
        elif a>=25 and a<27:
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

