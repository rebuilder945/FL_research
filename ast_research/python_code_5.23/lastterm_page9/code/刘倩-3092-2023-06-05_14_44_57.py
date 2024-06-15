class BMI
    def(self,sName,iAge,fHeight,fWeight):
        bmi.sName = name
        bmi.iAge = age
        bmi.fHeight = height
        bmi.fWeight = weight

        def getBMI(self):
            return bmi.fWeight / (bmi.fHeight**2)

        def getStatus(self):
            if bmi.getBMI() < 18:
                return underweight
            elif bmi.getBMI() >= 18 and bmi.getBMI()<25:
                return ideal
            elif bmi.getBMI()>=25 and bmi.getBMI()<27:
                return overweight
            else:
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

