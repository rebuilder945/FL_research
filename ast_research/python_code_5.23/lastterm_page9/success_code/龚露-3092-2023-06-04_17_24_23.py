class BMI:
    def __init__(bmi,sName,iAge,fHeight,fWeight):
        bmi.name=sName
        bmi.age=iAge
        bmi.height=fHeight
        bmi.weight=fWeight
    def getBMI(bmi,fHeight,fWeight):
        c=fWeight/(fHeight*fHeight)
        return c
    def getStatus(c):
        if c < 18:
            return underweight
        if 18 <= c < 25:
            return ideal
        if 25 <= c < 27:
            return overweight
        if 27 <= c:
            return obesity
    

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

