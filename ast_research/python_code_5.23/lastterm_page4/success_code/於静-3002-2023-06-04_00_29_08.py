lst=eval(input())
avg=sum(lst)/len(lst)
if sum(lst)%len(lst)==0:
    print(int(avg))
else:
    print("%.2f"%avg)
