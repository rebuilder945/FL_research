lst=eval(input())
ori=sum(lst)/len(lst)
avg=int(ori)
if ori>avg:
    print("%.2f"%ori)
else:
    print(int(ori))
