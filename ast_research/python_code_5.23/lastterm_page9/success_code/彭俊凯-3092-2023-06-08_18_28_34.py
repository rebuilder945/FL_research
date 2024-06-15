class BMI:
    def __init__(bmi,a,b,c,d):
        bmi.a=a
        bmi.b=b
        bmi.c=c
        bmi.d=d
    def name(bmi):
        return bmi.a
    def age(bmi):
        return bmi.b
    def getBMI(bmi):
        return bmi.c
    def getStatus(bmi):
        return bmi.d

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

