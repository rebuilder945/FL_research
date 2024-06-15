a = eval(input())
average = sum(a)/len(a)
b = average-int(average)
if b==0:
    print(int(average))
else:
    print("%.2f"%average)

