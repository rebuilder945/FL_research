from decimal import Decimal


ls = eval(input())
average = sum(ls)/len(ls)
if type(average) == int:
    average = Decimal(average).normalize()
    print(average)
else: print('%.2f'% average)
