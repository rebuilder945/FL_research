class BMI:
    def __init__(self,sName,fAge,fHeight,fWeight) :
        self.sName=sName
        self.fAge=fAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def getName(self):
        return self.sName
    name=getName()
    def getAge(self):
        return self.fAge
    age=getAge()
    def getHeight(self):
        return self.fHeight
    def getWeight(self):
        return self.fWeight
    def getBMI(self):
        return self.fWeight/(self.fHeight**2)
    def getStatus(self):
        if (self.fWeight/(self.fHeight**2))<18:
            return "underweight"
        elif (self.fWeight/(self.fHeight**2))>=18 and (self.fWeight/(self.fHeight**2))<25:
            return "ideal"
        elif (self.fWeight/(self.fHeight**2))>=25 and (self.fWeight/(self.fHeight**2))<27:
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

