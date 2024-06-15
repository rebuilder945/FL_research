def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def getBMI(self):
        return self.weight/self.height**2
    def getStatus(self):
        a=self.weight/self.height**2
        if a<18:
            return "underweight "
        elif a<25 and a>=18:
            return "ideal"
        elif a<27 and a>=25:
            return "overweigth"
        else:
            return "obesity"

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

