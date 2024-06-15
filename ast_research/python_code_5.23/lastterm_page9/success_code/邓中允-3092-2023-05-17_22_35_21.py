class BMI:
    def __init__(self,name,age,h,w):
        self.name=name
        self.age=age
        self.h=h
        self.w=w
    def getBMI(self):
        return self.w/(self.h**2)
    def getStatus(self):
        v=self.getBMI()
        if v< 18:   
            return "underweight" 

        if 18 <= v < 25: 
            return "ideal"

        if 25 <= v < 27:
            return "overweight"

        if 27 <= v:
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

