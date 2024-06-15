lst=eval(input())
average=sum(lst)/len(lst)
i="average"
if i.count('.')==0:
    print("%.0f"%average)
else:
    print("%2.f"%average)
