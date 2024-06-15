class BMI:
  def __init__(self,sName,iAge,fHeight,fWeight):
      self.sName=sName
      self.iAge=iAge
      self.fHeight=fHeight
      self.fWeight=fWeight
  def getBMI(self):
       return (self.fHeight)/(self.fWeight**2)
  def getStatus(self):
        if (self.fHeight)/(self.fWeight**2)<18:
                 return underweight
        if 25>(self.fHeight)/(self.fWeight**2)>=18:
                 return ideal
        if 27>(self.fHeight)/(self.fWeight**2)>=25:
                 return overweight
        if (self.fHeight)/(self.fWeight**2)>=27:
                 return obesity

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

