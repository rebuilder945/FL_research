class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.sName=sName
        self.iAge=iAge
        self.fHeight=fHeight
        self.fWeight=fWeight

    def name(self):
        return self.sName
    
    def age(self):
        return self.iAge
    
    def getBMI(self):
        return self.fWeight/self.fHeight**2
    
    def getStatus(self):
        bmi=self.fWeight/self.fHeight**2
        if bmi < 18:
            return "underweight"
        if bmi >=18 and bmi <25:
            return 'ideal'
        if bmi >=25 and bmi <27:
            return "overweight"
        if bmi >=27:
            return 'obesity'
        

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

