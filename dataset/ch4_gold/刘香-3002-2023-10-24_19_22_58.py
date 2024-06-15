ls=eval(input())
m=int(sum(ls))
n=len(ls)
sAverage=m/n
if sAverage % 1 ==0 :
    print(sAverage)
else:
    print("%.2f"%(sAverage))
