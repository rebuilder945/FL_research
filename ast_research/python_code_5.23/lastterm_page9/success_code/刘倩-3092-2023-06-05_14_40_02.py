class BMI:
    def __init__(self, sName, iAge, fHeight, fWeight):
        self.__sName = sName
        self.__iAge = iAge
        self.__fHeight = fHeight
        self.__fWeight = fWeight

    def getBMI(self):
        return self.__fWeight / (self.__fHeight ** 2)

    def getStatus(self):
        if self.getBMI() < 18:
            return "underweight"
        elif 18 <= self.getBMI() < 25:
            return "ideal"
        elif 25 <= self.getBMI() < 27:
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

