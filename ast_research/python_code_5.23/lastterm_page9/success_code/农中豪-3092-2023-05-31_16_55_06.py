class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.height=fHeight

        self.weight=fWeight

        self.name=sName
        self.age=iAge

    def getBMI(self):
        c = self.weight / pow(self.height,2)
        return c

    def getStatus(self):
        d = self.weight / pow(self.height,2)
       
        if d < 18.5:
            return "超轻"
        elif ((d >= 18.5 and d <= 25) or (d >= 18.5 and d<= 24)):
             return  "标准"
        elif ((d > 25 and d <= 30) or (d > 24 and d <= 28)):
            return  "超重"
        elif ((d > 30) or (d > 28)):
             return "肥胖"


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

