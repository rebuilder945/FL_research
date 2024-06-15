class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def getBMI(self):
        bmi_num=self.weight/((self.height)**2)
        return bmi_num
    def getStatus(self):
        bmi_num=self.getBMI()
        if bmi_num<18:
            return "underweight"
        elif bmi_num<25 and bmi_num>=18:
            return "ideal"
        elif bmi_num<27 and bmi_num>=25:
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

