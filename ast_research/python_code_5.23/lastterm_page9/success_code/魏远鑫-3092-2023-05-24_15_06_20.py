class BMI:
    def __init__(self,mingji,nianning,shengao,tizhong,):
        self.mingzi=sName
        self.nianning=iAge
        self.shengao=fHeight
        self.tizhong=fWeight
    def getBMI(self):
        return self.tizhong/self.shengao*self.shengao
    def getStatus(self):
        if bmi<18:
            return underweight 
        elif 18<= bmi<25:
            return ideal
        elif 25 <=bmi<27:
            return overweight
        elif 27<=bmi:
            return obesity

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

