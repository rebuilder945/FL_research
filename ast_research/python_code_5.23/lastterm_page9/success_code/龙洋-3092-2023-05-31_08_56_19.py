class BMI:
    def __init__(self,na,ag,he,we):
        self.name=na
        self.age=ag
        self.weight=we
        self.hight=he
        self.result=0
    def getBMI(self):
        self.result=self.weight/((self.hight)**2)
        return self.result
    def getStatus(self):
        if self.result<18:
            return 'underweight'
        elif self.result<25:
            return 'ideal'
        elif self.result<27:
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

