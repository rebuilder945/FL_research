class BMI:
    def _init_(self,sName,iAge,fHight,fWeight):
        self.name=sName
        self.age=iAge
        self.hight=fHight
        self.weight=fWeight
    
    def getBMI(self):
        return self.Weight/(self.Height**2)
    
    def getStatus(self):
        value=self.Weight/(self.Height**2)
        if value<18:
            return "超轻"
        elif value>=18 and value<25:
            return "正常"
        elif value>=25 and value<27:
            return "超重"
        elif  value>=27:
            return "肥胖"

     def getBMI(self):
          b=fWeight/(fHeight*fHeight)
          return b

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

