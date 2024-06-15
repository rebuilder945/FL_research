class BMI:
    def __init__(self, sname, iage, fheight, fweight):
        self.name = sname
        self.age = iage
        self.height = fheight
        self.weight = fweight
        self.bmit = fweight/(fheight ** 2)
    def getBMI(self):
        return self.bmit
    def getStatus(self):
        if self.bmit < 18:
            return "underweight"
        elif self.bmit < 25:
            return "ideal"
        elif self.bmit < 27:
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

