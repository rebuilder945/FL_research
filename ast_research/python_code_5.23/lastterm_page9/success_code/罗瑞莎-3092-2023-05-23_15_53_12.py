class BMI:
    def __init__(bmi,name,age,height,weight):
        bmi.name = name
        bmi.age = age
        bmi.fHeight = height
        bmi.fWeight = weight

    def getBMI(bmi):
        return(bmi.fWeight/(bmi.fHeight**2))

    def getStatus(bmi):
        if bmi.getBMI()<18:
            return("underweight")
        if bmi.getBMI()>=18 and bmi.getBMI()<25:
            return("ideal")
        if bmi.getBMI()>=25 and bmi.getBMI()<27:
            return("overweight")
        if bmi.getBMI()>=27 and bmi.getBMI:
            return("obesity")

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

