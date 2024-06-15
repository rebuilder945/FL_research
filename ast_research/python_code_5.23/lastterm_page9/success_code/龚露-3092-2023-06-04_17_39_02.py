class BMI:
    def __init__(self,sName='N/A',iAge=0,fHeight=0,fWeight=0):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        c= self.weight/(self.height**2)
        return c
    def getStatus(self):
        c= self.weight/(self.height**2)
        if c < 18:
            return underweight
        if 18 <= c < 25:
            return ideal
        if 25 <= c < 27:
            return overweight
        if 27 <= c:
            return obesity
    

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

