lst=eval(input())
avg=sum(lst)/len(lst)
if avg-int(avg)==0:
    print(int(avg))
else:
    print(round(avg,2))
