def __init__(self,sName="N/A",iAge=0,fHeight=0,fWeight=0):
        self.name=sName
        self.age=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def  getBMI(self):
        return float(self.fWeight/float(self.fHeight)**2)
    def getStatus(self):
        if self.fWeight/float(self.fHeight)**2<18:
            return "underweight"
        elif 18<=self.fWeight/float(self.fHeight)**2<25:
            return "ideal"
        elif  25<=self.fWeight/float(self.fHeight)**2<27:
            return "overweight"
        else:
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

