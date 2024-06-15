class BMI:
    def __init__(self,sn,ia,fh,fw):
        self.name=sn
        self.age=ia
        self.fHeight=fh
        self.fWeight=fw
    def getBMI(self):
        return self.fWeight/self.fHeight**2
    def getStatus(self):
        a=self.getBMI()
        if a<18:
            return "underweight"
        elif a<25:
            return "ideal"
        elif a<27:
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

