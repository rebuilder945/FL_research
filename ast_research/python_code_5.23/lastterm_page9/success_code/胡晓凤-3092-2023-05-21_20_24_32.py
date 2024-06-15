class BMI:
    def __init__(self,name,age,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def getBMI(self):
        value=self.fWeight/(self.fHeight)**2
        return value
    def getStatus(self,value):
        if value<18:
            return ("underweight")
        elif 18<=value<25:
            return ("ideal")
        elif 25<=value<27:
            return ("overweight")
        else:
            return ("obesity")

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

