class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self._height=height
        self._weight=weight
    def getBMI(self):
        return self._weight/pow(self._height,2)
    def getStatus(self):
        if self._weight/pow(self._height,2)< 18:
            return "underweight"
        elif 18 <=self._weight/pow(self._height,2) < 25:
            return  "ideal"
        elif 25 <= self._weight/pow(self._height,2)< 27:
            return  "overweight"
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

