ls=eval(input())
m=(sum(ls))
n=len(ls)
sAverage=m/n
if sAverage % 1 ==0 :
    print(int(sAverage))
else:
    print("%.2f"%(sAverage))
