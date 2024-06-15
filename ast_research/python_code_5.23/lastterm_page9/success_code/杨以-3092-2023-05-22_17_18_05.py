class BMI:
    def __init__(self,sname,sage,sheight,sweight):
        self.name=sname
        self.age=int(sage)
        self.height=float(sheight)
        self.weight=float(sweight)
    def getBMI(self):
        return self.weight/(self.height)**2
    def getStatus(self):
        if self.getBMI()<18:
            return 'underweight'
        elif 18<=self.getBMI()<25:
            return 'ideal'
        elif 25<=self.getBMI()<27:
            return 'overweight'
        elif 27<=self.getBMI():
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

