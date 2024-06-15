class BMI:
    def__int__(self,sName,iAge,fHeight,fWeight):
        self.sName=sName
        self.iAge=iAge
        self.fHeight=fHeight
        self.fWeight =fWeight 


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

