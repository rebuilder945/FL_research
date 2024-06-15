lst=eval(input())
aver=sum(lst)/len(lst)
a=int(aver)
if a<aver:
    print("%.2f"%aver)
else:
    print(a)
