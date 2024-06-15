class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=float(age)
        self.height=float(height)
        self.weight=float(weight)
    def getBMI(self):
        return float(self.weight/self.height**2)
    def getStatus(self):
        if bmi.getBMI(self)<18:
            return 'underweight'
        elif 18<=bmi.getBMI(self)<25:
            return 'ideal'
        elif 25<=bmi.getBMI(self)<27:
            return 'overweight'
        else:
            obesity

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

