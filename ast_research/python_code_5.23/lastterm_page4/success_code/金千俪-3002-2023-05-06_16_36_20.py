lst=eval(input())
avege=sum(lst)/len(lst)
if sum(lst)%len(lst)==0:
    print(int(avege))
else:
    print("%.2f"%(avege))
