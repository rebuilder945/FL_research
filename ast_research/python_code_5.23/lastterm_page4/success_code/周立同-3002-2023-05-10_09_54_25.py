lst=eval(input())
avg=sum(lst)/len(lst)
if avg==int(avg):
    print(int(avg))
else:
    avg2=round(avg,2)
    avg3=("%.2f"%(avg2))
    print(avg3)
