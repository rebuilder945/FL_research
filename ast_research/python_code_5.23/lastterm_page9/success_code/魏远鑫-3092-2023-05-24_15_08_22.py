class BMI:
    def __init__(self,name,age,shengao,tizhong,):
        self.name=sName
        self.age=iAge
        self.shengao=fHeight
        self.tizhong=fWeight
    def getBMI(self):
        return self.tizhong/self.shengao*self.shengao
    def getStatus(self):
        if int(bmi)<18:
            return underweight 
        elif 18<= int(bmi)<25:
            return ideal
        elif 25 <=int(bmi)<27:
            return overweight
        elif 27<=int(bmi):
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

