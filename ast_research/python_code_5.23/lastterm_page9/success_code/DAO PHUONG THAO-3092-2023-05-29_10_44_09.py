class BMI:
    def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getStatus(self):
        m=fWeight/(fHeight**2)
        if m<18:
            return ("超轻")
        elif m>=18 and m<25:
            return ("标准")
        elif m>=25 and m<27:
            return ("超重")
        else:
            return ("肥胖")
    def getBMI(self):
        n=fWeight/(fHeight**2)
        return n


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

