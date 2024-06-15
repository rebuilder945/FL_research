class Stock:
    "Stock Information Class"
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.sCode=sCode
        self.sName=sName
        self.priceYesterday=priceYesterday
        self.priceToday=priceToday
    def getCode(self):
        return self.sCode
    def getName(self):
        return self.sName
    def getPriceYesterday(self):
        return self.priceYesterday
    def getPriceToday(self):
        return self.priceToday
    def setPriceYesterday(self,a):
        self.priceYesterday=a
        return self.priceYesterday
    def setPriceToday(self,b):
        self.priceToday=b
        return self.priceToday
    def getChangePercent(self):
        return (self.priceToday-self.priceYesterday)/self.priceYesterday

sName = input()  
iAge = int(input())
fHeight = eval(input()) #in meter
fWeight = eval(input()) #in kg
bmi=BMI(sName,iAge,fHeight,fWeight)
print("Name:",bmi.name)
print("Age:",bmi.age)
print("BMI = %.3f" % bmi.getBMI())
print("Result =",bmi.getStatus())

