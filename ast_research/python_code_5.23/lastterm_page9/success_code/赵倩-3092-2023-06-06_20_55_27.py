class BMI:
    def __init__(bmi,name,age,height,weight):
        bmi.name=sName
        bmi.age=iAge
        bmi.height=fHeight
        bmi.weight=fWeight
    def getBMI(bmi):
        l= bmi.weight/(bmi.height)**2
        return l
    def getStatus(bmi):
        l=bmi.weight/(bmi.height)**2
        if l<18:
            return "underweight"
        elif l<25:
            return "ideal"
        elif l<27:
            return"overweight"
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

