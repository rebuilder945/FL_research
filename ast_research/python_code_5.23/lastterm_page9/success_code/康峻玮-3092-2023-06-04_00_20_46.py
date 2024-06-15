class BMI:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def getBMI(self):
        return self.weight / (self.height ** 2)
    
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18:
            return 'underweight'
        elif bmi < 25:
            return 'ideal'
        elif bmi < 27:
            return 'overweight'
        else:
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

