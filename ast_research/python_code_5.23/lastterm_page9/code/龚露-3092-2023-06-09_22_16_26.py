class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def bmi.name(self):
        return self.name
    def bmi.age(self):
        return self.age
    def bmi.getBMI(self,fHeight,fWeight):
        c=self.weight/(self.height)**2
    def bmi.getStatus(self,fHeight,fWeight):
        c=self.weight/(self.height)**2
        if c<18:
            return 'underweight'
        elif  18<=c<25:
            return ideal
        elif 25<=c<27:
            return overweight
        else:
            obesity

  

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

