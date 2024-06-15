class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        return self.weight/(self.height**2)
    def getStatus(self):
        a=BMI.getBMI(self)
        if a<18:
            print("underweight")
        elif 18<=a<25:
            print("ideal")
        elif 25<=a<27:
            print("overweight")
        else:
            print("obesity")

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

