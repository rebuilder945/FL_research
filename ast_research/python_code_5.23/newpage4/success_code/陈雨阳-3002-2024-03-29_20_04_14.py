from audioop import avg
lst=eval(input())
oringinal=sum(lst)/len(lst)
avg=int(oringinal)
if oringinal>avg:
    print("%.2f"%oringinal)
else:
    print(avg)
