class BMI:
    def __init__(bmi,sName,iAge,fHeight,fWeight ):
        bmi.name=sName
        bmi.age=iAge
        bmi.Height=fHeight
        bmi.Weight=fWeight
    def getBMI(bmi):
        return bmi.Weight / (bmi.Height ** 2)
    def getStatus(bim):
        if bmi.Weight / (bmi.Height ** 2)<18:
            return "underweight"
        elif 18<=bmi.Weight / (bmi.Height ** 2)<25:
            return "ideal"
        elif 25<=bmi.Weight / (bmi.Height ** 2)<27:
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

