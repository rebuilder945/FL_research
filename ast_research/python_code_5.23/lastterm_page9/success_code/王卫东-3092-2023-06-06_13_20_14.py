class BMI:
    def _init_(self,a,b,c,d):
        self.name=a
        self.age=b
        self.height=c
        self.weight=d
    def getBMI(self):
        return self.weight/(self.height**2)
    def getStatus(self):
        if self.getBMI()<18:
            return 'underweight'
        elif self.getBMI()<25 and self.getBMI()>=18:
            return 'ideal'
        elif self.getBMI()<27 and self.getBMI()>=25:
            return 'overweight'
        elif self.getBMI()>=27:
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

