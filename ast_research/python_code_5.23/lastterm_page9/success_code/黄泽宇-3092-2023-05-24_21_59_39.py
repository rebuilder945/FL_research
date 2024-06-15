class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.sName=sName
        self.iAge=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight
    def name(self):
        return self.sName
    def age(self):
        return sele.iAge
    def getBMI(self,a,b):
        a=self.fHeigh
        b=self.fWeight
        return b/(a**2)
    def getStatus(self,a,b):
        a=self.fHeigh
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

