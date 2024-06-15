class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.fHeight=height
        self.fWeight=weight
    # def name(self):
    #     return self.sName
    # def age(self):
    #     return self.iAge
    def getBMI(self):
        return self.fWeight/(self.fHeight* self.fHeight)
    def getStatus(self):
        value=self.getBMI()
        if value<18:
            return "underweight"
        elif value>=18 and value<25:
            return "ideal"
        elif value>=25 and value<27:
            return "overweight"
        elif value>=27:
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

