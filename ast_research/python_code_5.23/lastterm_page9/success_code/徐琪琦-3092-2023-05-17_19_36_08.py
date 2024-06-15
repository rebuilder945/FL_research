class BMI:    
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def getBMI(self):
        value = self.weight/(self.height**2)
        return value3
    def getStatus(self):             #注意getStatus(self,value)也没用，必须在getStatus里面再定义一遍value，因为value是局部变量   
        value = self.weight/(self.height**2) #这里的参数无需写上weight什么的了
        if value <18:
            return"underweight"
        elif value >= 18 and value<25:
            return "ideal"
        elif value >= 25 and value<27:
            return "overweight"
        elif value >= 27:
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

