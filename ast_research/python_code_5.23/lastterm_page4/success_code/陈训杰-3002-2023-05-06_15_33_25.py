lst=eval(input())
ave=sum(lst)/len(lst)
if sum(lst)%len(lst)==0:
    print("%d" %ave)
else:
    print("%.2f" %ave)

