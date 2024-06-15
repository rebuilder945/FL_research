lst = eval(input())
sum = 0
for i in lst:
    sum +=i
l = len(lst)
average = sum/l
if type(average) == float:
    print("%.2f"%average)
else:
    print("%d"%average)
