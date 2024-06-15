class BMI:
    def __init__(self,sName,iAge,fWeight,fHeight):
        self.name=sName
        self.age=iAge
        self.weight=fWeight
        self.height=fHeight
    def getBMI(self):
        
        return (fWeight/fHeight**2)
    def getStatus(self):
        if (fWeight/fHeight**2)<18:
            return "underweight"
        elif (fWeight/fHeight**2)>=18 and (fWeight/fHeight**2)<25:
            return "ideal"
        elif (fWeight/fHeight**2)>=25 and (fWeight/fHeight**2)<27:
            return "overweight"
        elif (fWeight/fHeight**2)>=27:
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

