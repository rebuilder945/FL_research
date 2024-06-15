class BMI:
      def __init__(self,sName,iAge,fHeight,fWeight):
            self.name = sName
            self.age= iAge
            self.height=fHeight
            self.weight=fWeight
      def getBMI(self):
            return (self.weight)/(self.height**2)
      def getStatus(self):
            result= self.getBMI()
            if(result< 18):
                 t = "underweight"
           elif (result<25) :
                 t="ideal"
           elif(result<27):
                 t="overweight"
           else:
                 t="obesity"
           return t

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

