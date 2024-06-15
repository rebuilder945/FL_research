class BMI:
    def __init__(self,name,age,height,weight):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        getBMI=self.weight/self.height**2
        return getBMI
    def getStatus(self):
        getBMI=self.weight/self.height**2
        if getBMI<18:
            return 'underweight'
        elif 18<=getBMI<25:
            return 'ideal'
        elif 25<=getBMI<27:
            return 'overweight'
        elif 27<=getBMI:
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

