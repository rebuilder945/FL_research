class BMI:
 
    def __init__(self, name: str, age: int, height: float, weight: float):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def getBMI(self) -> float:
      
        return self.weight / self.height ** 2

    def getStatus(self) -> str:
       
        bmi = self.getBMI()
        if bmi < 18:
            return BMI.underwight
        elif bmi < 25:
            return BMI.ideal
        elif bmi < 27:
            return BMI.overweight
        else:
            return BMI.obesity


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

