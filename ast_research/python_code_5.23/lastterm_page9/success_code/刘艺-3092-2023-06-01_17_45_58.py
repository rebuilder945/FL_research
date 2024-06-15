class BMI:
    def __init__(self,sname,iAge,c,d):
        self.name = sname
        self.age = iAge
        self.c = c
        self.d = d
    def getBMI(self):
        self.BMI =  self.d/(self.c)**2
        return self.BMI
    def getStatus(self):
        if 18<= self.BMI <25:
            return "ideal"
        elif 25<= self.BMI < 27:
            return "overweight"
        elif 27<= self.BMI:
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

