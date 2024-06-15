class BMI:
    def __init__(self,xingming,nianling,shengao,tizhong):
        self.name = xingming
        self.age = nianling
        self.shengao = shengao
        self.tizhong = tizhong

    def getBMI(self):
        bmi = self.tizhong/(self.shengao**2)
        return bmi

    def getStatus(self):
        bmi = self.getBMI()
        if bmi<18 :
            return 'underweight'
        elif 18<=bmi<25:
            return 'ideal'
        elif 25<=bmi<27:
            return 'overweight'
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

