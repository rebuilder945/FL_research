class BMI:
    def __init__(self,name,age,height,weight):
        self.sName=name
        self.iAge=age
        self.fHeight=height
        self.fWeight=weight
    def name(self):
        return self.sName
    def age(self):
        return self.iAge
    def getBMI(self):
        sBMI=float(self.fWeight)/(self.fHeight)**2
        return sBMI
    def getStatus(self):   
        sBMI=float(self.fWeight)/(self.fHeight)**2
        if sBMI<18:
            return "underweight"
        if 18 <= sBMI < 25:
            return "ideal"
        if 25 <= sBMI < 27:
            return "overweight"
        if 27 <= sBMI:
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

