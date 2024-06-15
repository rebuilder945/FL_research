class BMI:
    def _init_(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        b=fWeight/fHeight/fWeight
        return b
    def getStatus():
        b=fWeight/fHeight/fWeight
        if b<18:
            return "underweight"
        if 18<=b<25:
            return "ideal"
        if 25<=b<27:
            return "overweight"
        if 27<=b:
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

