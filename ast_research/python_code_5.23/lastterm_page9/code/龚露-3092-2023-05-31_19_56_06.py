class BMI:
    def __init__(bmi,sName,iAge,fHeight,fWeight):
        bmi.name=sName
        bmi.age=iAge
        bmi.height=fHeight
        bmi.weight=fWeight
    def getBMI(bmi,fHeight,fWeight):
        c=fWeight/(fHeight*fHeight)
        print(“%.3f”%c)
    def getStatus(c):
        if c < 18:
            print（“underweight”） 
        if 18 <= c < 25:
            print ("ideal")
        if 25 <= c < 27:
            print("overweight")
        if 27 <= c:
            print("obesity")
    

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

