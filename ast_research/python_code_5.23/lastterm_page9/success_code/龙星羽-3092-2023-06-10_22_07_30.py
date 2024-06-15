class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        BMI=self.weight/(self.height*self.height)
        return BMI 
    def getStatus(self):
        if BMI.getBMI(self) < 18  :
            return "underweight "
        if 18 <=BMI.getBMI(self) < 25:
            return "ideal"
        if 25 <= BMI.getBMI(self) < 27:
            return 'overweight'
        if 27 <= BMI.getBMI(self):
            return   'obesity'

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

