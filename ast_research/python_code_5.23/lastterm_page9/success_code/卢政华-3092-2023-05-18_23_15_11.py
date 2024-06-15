class BMI:
    UNDERWEIGHT = "underweight"
    IDEAL = "ideal"
    OVERWEIGHT = "overweight"
    OBESITY = "obesity"

    def __init__(self, name: str, age: int, height: float, weight: float):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def getBMI(self) -> float:
        """
        计算身体质量指数
        """
        return self.weight / self.height ** 2

    def getStatus(self) -> str:
        """
        计算评价结果
        """
        bmi = self.getBMI()
        if bmi < 18:
            return BMI.UNDERWEIGHT
        elif bmi < 25:
            return BMI.IDEAL
        elif bmi < 27:
            return BMI.OVERWEIGHT
        else:
            return BMI.OBESITY


sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())
