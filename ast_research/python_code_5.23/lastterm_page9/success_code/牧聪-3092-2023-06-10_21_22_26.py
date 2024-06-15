class BMI:
    def __init__(bmi,sName,iAge,fHeight,fWeight):
        bmi.name=sName
        bmi.age=iAge
        bmi.fHeight=fHeight
        bmi.fWeight=fWeight
    def getBMI(bmi):
        BMI=bmi.fWeight/bmi.fHeight**2
        return BMI
    def getStatus(bmi):
        BMI=bmi.fWeight/bmi.fHeight**2
        if BMI<18:
            return "underweight"
        elif 18<=BMI<25:
            return "ideal"
        elif 25<=BMI<27:
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

