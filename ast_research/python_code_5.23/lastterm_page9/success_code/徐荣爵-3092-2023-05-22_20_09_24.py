class BMI:
    def __init__(self,name1,age1,height1,weight1):
        self.name = name1
        self.age = age1
        self.height = height1
        self.weight = weight1
    def getBMI(self):
        return self.weight/self.height ** 2
    def getStatus(self):
        k = self.getBMI()
        if k < 18:
            return 'underweight'
        elif k < 25:
            return 'ideal'
        elif k < 27:
            return 'ideal'
        else:
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

