class BMI:
    def__init__(self,name,age,height,weight):
        self.__name=name
        self.__age=age
        self.__height=height
        self.__weight=weight
    def getBMI(self):
        a=self.__weight/(self.__height**2)
    return a
    def getStatus(self):
        BMI=self.__weight/(self.__height**2)
        if BMI<18:
            print("underweight")
        elif BMI>=18 and BMI<25:
            print("ideal")
        elif BMI>=25 and BMI<27:
            print("overweight")
        else:
            print("obesity")
    print()

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

