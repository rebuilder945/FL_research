ls=eval(input())
m=sum(ls)
n=len(ls)
sAverage=m/n
print(type(sAverage))
if sAverage % 1 ==0 :
    print(sAverage)
else:
    print("%.2f"%(sAverage))
