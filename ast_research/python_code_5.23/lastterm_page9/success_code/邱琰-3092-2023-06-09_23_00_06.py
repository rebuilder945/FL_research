class BMI:
    def __init__(self,name,age,height,weight):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        n=self.weight/(self.height)**2
        return n
    def getStatus(self):
        n=self.weight/(self.height)**2
        if n<18:
            return 'underweight'
        if 18<=n<25:
            return 'ideal'
        if 25<=n<27:
            return 'overweight'
        if 27<=n:
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

