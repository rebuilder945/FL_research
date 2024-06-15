class BMI:
    def__init__(self,sName,iAge,fHeight,fWeight):
        self.sName=sName
        self.iAge=iAge
        self.iHeight=iHeight
        self.fWeight=fWeight
    def getBMI(self):
        return (self.fWeight/(self.iHeight*self.iHeight))
    def getStatus(self):
        bmi=self.fWeight/(self.iHeight*self.iHeight)
        if bmi<18:
            result="underweight"
        elif 18<=bmi<25:
            result="ideal"
        elif 25<=bmi<27:
            result="overweight"
        elif 27<=bmi:
            result="obesity"
        return result

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

