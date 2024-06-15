    def __init__(self,name,age,height,weight):                      
        self.name=name
        self.age=age
        self.fHeight=height
        self.fWeight=weight
    def getBMI(self):
        bmi=self.fWeight/(self.fHeight)**2
        return bmi
    def getStatus(self):
        if (self.fWeight/(self.fHeight)**2)<18:
            return "underweight"
        if 18<(self.fWeight/(self.fHeight)**2)<25:
            return "ideal"
        if 25<(self.fWeight/(self.fHeight)**2)<27:
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

