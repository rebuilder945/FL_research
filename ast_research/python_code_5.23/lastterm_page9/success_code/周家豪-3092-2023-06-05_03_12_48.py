class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.h=height
        self.w=weight
    def getBMI(self):
        return self.w/(self.h)**2
    def getStatus(self):
        if self.w/(self.h)**2<18:
            return('underweight')
        elif self.w/(self.h)**2>=18 and self.w/(self.h)**2<=25:
            return('ideal')
        elif self.w/(self.h)**2>=25 and self.w/(self.h)**2<=27:
            return('overweight')
        else:
            return('obesity')

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

