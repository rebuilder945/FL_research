lst=eval(input())
average=sum(lst)/len(lst)
ndot=sum(lst)//len(lst)
chic=average-ndot
if chic==0:
    print("%d"%average)
else:
    print("%.2f"%average)
