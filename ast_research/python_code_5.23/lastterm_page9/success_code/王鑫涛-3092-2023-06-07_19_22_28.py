class BIM:
    def __init__(self,name='N/A',age=0,height=0,weight=0):
        self.name=name
        self.age=int(age)
        self.weight=float(weight)
        self.height=float(height)
        self.BIM=self.weight/(self.height**2)
    def getBIM(self):
        return self.BIM
    def getStatus(self):
        a=self.BIM
        if a<18:
            return 'underweight'
        elif a<25:
            return 'ideal'
        elif a<27:
            return 'overweight'
        else:
            return 'obesityt'


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

