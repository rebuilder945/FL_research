class BMI:
    def __init__(self,sName="N/A",iAge="N/A",fHeight="N/A",fWeight="N/A"):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        return (self.weight/(self.height**2))
    def getStatus(self):
        if (self.weight/(self.height**2))<18:
            return "underweight"
        elif (self.weight/(self.height**2))<25:
            return "ideal"
        elif (self.weight/(self.height**2))<27:
            return "overweight"
        else :
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

