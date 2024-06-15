class BMI:
    def __init__(bmi,sName,iAge,fHeight,fWeight):
        bmi.sName=sName
        bmi.iAge=iAge
        bmi.fHeight=fHeight
        bmi.fWeight=fWeight
    def name(bmi):
        return bmi.sName
    def age(bmi):
        return bmi.iAge
    def getBMI(bmi):
        bmi.h=bmi.fWeight/bmi.fHeight**2
        return bmi.fWeight/bmi.fHeight**2
    def getStatus(bmi):
        if bmi.h<18:
            return 'underweight'
        if 18<=bmi.h<25:
            return 'ideal'
        if 25<=bmi.h<27:
            return 'overweight'
        if 27<=bmi.h:
            return 'obesity'


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

