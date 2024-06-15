#class Stock
class BMI:
    def __init__(self,name,age,height,weight):
        self.sName=name
        self.iAge=age
        self.fHeight=height
        self.fWeight=weight
    def getBMI(self):
        return (self.fWeight/self.fHeight**2)
    def getStatus(self):
        if BMI<18:
            return "underweight"
        elif BMI>=18 and BMI<25:
            return "ideal"
        elif BMI>=25 and BMI<27:
            return "overweight"
        elif BMI>=27:
            return "obesity"


sCode = input() #Stock Code
sName = input() #Stock Name
priceYesterday = float(input())  #Price/Yesterday
priceToday = float(input())  #Price Today
s = Stock(sCode,sName,priceYesterday,priceToday)
print("Code:",s.getCode())
print("Name:",s.getName())
print("Price/Yesterday:%.2f\nPrice Today:%.2f" % (s.getPriceYesterday(),s.getPriceToday()))
s.setPriceYesterday(50.25)
print("Edit Price/Yesterday To:%.2f" % 50.25)
print("Price Change Percentage:%.2f%%" % (s.getChangePercent()*100))
print(Stock.__doc__)


