class BMI:
    
    def __init__(self,sName='N/A',iAge='N/A',fHeight=0,fWeight=0):
        self.name = sName
        self.age = iAge
        self.weight = fWeight
        self.height = fHeight
        self.BMI = 0
        
    def getBMI(self):
        self.BMI = self.weight/2**(self.height)
        return self.BMI
    
    def getStatus(self):    
        word = self.BMI
        if word < 18:
            return 'underweight'
        if 18 <= word <25:
            return 'ideal'
        if 25 <= word < 27:
            return 'overweight'
        if 27 <= word:
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

