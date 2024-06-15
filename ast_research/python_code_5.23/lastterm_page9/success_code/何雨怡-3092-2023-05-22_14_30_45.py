class BMI:
    def __init__(self,name="N/A",age="N/A",height="N/A",weight="N/A"):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        result=(self.weight)/(self.height)**2
        return result
    def getStatus(self):
        num=BMI.getBMI(self)
        if num<18:
            return "underweight"
        elif 18<=num<25:
            return "ideal"
        elif 25<=num<27:
            return "overweight"
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

