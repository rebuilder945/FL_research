class BMI:
    def __init__(self,sName ,iAge,fHeight,fWeight):
        name=sName
        age=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def getBMI(self):
        return self.fWeight/(self.fHeight**2)
    def getStatus(self):
        if self.fWeight/(self.fHeight**2)<18:
            return underweight 
        if self.fWeight/(self.fHeight**2)>=18 and self.fWeight/(self.fHeight**2)<25:
            return ideal
        if self.fWeight/(self.fHeight**2)>=25 and self.fWeight/(self.fHeight**2)<27:
            return overweight
        if self.fWeight/(self.fHeight**2)>=27:
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

