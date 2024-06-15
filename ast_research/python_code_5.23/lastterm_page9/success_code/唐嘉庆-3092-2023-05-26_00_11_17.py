class BIM:
   def __init__(self,sName,iAge,fHeight,fWeight):
        self.name=sName
        self.age=iAge
        self.height= fHeight
        self.weight=fWeight
   def getBMI(self):
        return ( self.weight/(self.height**2))
   def getStatus(self):
        if getBMI < 18  :
            return 'underweight' 
        if 18 <= getBMI < 25 :
            return 'ideal'
        if 25 <= getBMI < 27 :
            return 'overweight'
        if 27 <= getBMI  :  
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

