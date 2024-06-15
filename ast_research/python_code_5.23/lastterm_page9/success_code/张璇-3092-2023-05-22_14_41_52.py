class BMI:
    def __init__(self):
        self.name=sName
        self.age=iAge
        self.height=fHeight
        self.weight=fWeight
    def getBMI(self):
        a=self.weight/self.height**2
        print(a)
    def getstatus(self):
        b=self.weight/self.height**2
        if b<18:
            print('underweight')
        elif 18<=b<25:
            print('ideal')
        elif 25<=b<27:
            print('overweight')
        elif 27<=b:
            print('obesity')


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

