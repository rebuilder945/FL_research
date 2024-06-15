lst=eval(input())
average=sum(lst)/len(lst)
if average%1==0:
    print("%.0f"%average)
else:
    print("%2.f"%average)
