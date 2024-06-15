class BMI:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.fHeight=height
        self.fWeight=weight
    def getBMI(self):
        return (self.fWeight/(self.fHeight*self.fHeight))
    def getStatus(self):
        if   self.fWeight/(self.fHeight*self.fHeight)<18:
            return "underweight"
        elif self.fWeight/(self.fHeight*self.fHeight)>=18 and self.fWeight/(self.fHeight*self.fHeight)<25:
            return "ideal" 
        elif self.fWeight/(self.fHeight*self.fHeight)>=25 and self.fWeight/(self.fHeight*self.fHeight)<27:
           return "overweight"
        else:
           return"obesity"

                 


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

