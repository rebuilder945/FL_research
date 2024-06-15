a=eval(input())
sum(a)
average=sum(a)/len(a)
if average==int:
    print("%d"%average)
else:
    print("%.2f"%average)
