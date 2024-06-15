class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def getBMI(self):
        return self.weight/(self.height*self.height)
    def getStatus(self):
        if  self.getBMI()>=27:
            return("obesity")
        if 27>self.getBMI()>=25:
            return("overweight")
        if  self.getBMI()<18:
            return("underweight")
        if 18<=self.getBMI()<25:
            return("ideal")

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

