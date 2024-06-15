class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.sname=sName
        self.sage=iAge
        self.sheight=fHeight
        self.sweight=fWeight

    def getBMI(self):
        a=self.sweight/(self.sheight**2)
        return a

    def getStatus(self):
        a=self.sweight/(self.sheight**2)
        if a < 18:
            return "underweight" 

        elif 18 <= a < 25:
            return "ideal"

        elif 25 <= a < 27:
            return  "overweight"

        elif 27 <= a:
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

