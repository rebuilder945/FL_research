class BMI:
    def __init__(self,name,age,height,weight):
        self.name=str(name)
        self.age=age
        self.height=height
        self.weight=weight
    def getBMI(self):
        return(self.weight/(self.height**2))
    def getStatus(self):
        if self.getBMI()<18:
            return "underweight"
        if self.getBMI()>=18 and self.getBMI()<25:
            return "ideal"
        if self.getBMI()>=25 and self.getBMI()<27:
            return "overweight"
        if self.getBMI()>=27:
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

