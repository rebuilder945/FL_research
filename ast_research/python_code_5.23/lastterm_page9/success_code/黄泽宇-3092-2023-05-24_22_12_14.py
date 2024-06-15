class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
   
    def getBMI(self):
        a=self.fHeight
        b=self.fWeight
        return b/(a**2)
    def getStatus(self):
        a=self.fHeight
        b=self.fWeight
        c=b/(a**2)
        if c<18:
            return "underweight"
        elif c>=18 and c<25:
            return "ideal"
        elif c>=27:
            return "obesity"
        else:
            return "overweight"

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

