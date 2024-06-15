class BMI:
    def __init__(self,sName,fAge,fHeight,fWeight) :
        self.sName=sName
        self.fAge=fAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def name(self):
        return self.sName
    def age(self):
        return self.fAge
    def getHeight(self):
        return self.fHeight
    def getWeight(self):
        return self.fWeight
    def getBMI(self):
        return self.fWeight/(self.fHeight**2)
    def getStatus(self):
        if BMI<18:
            return "underweight"
        elif BMI>=18 and BMI<25:
            return "ideal"
        elif BMI>=25 and BMI<27:
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

