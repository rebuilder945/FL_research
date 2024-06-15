class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.bmi= self.weight/(self.height)**2
    def getBMI(self):        
        return self.bmi
    def getStatus(self):
        if self.bmi<18:
            return "underweight"
        elif self.bmi<25:
            return "ideal"
        elif self.bmi<27:
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

