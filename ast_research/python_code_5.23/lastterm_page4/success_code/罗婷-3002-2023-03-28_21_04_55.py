lst=eval(input())
average=sum(lst)/len(lst)
aver=sum(lst)//len(lst)
cha=average-aver
if cha==0:
    print("%d"%average)
else:
    print("%.2f"%average)
