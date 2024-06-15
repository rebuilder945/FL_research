class BMI:
    def __init__(s,sName,iAge,fHeight,fWeight):
        s.name=sName
        s.age=iAge
        s.h=fHeight
        s.w=fWeight
    def getBMI(s):
        return s.w/(s.h)**2
    def getStatus(s):
        a=getBMI(s)
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

