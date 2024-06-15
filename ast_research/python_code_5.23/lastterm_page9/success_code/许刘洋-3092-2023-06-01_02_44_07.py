class BMI:
    def __init__(self,name,age,fHeight,fWeight):
        self.name=name
        self.age=age
        self.fHeight=fHeight
        self.fweight=fWeight
    def getBMI(self):
        return fweight/fHeight**2
    def getStatus(self):
        x=self.getBMI()
        if x<18:
            return"underweight"
        if 18<=x<25:
            return"ideal"
        if 25<=x<27:
            return"underweight"
        if x>=27:
            return"obesity"

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

