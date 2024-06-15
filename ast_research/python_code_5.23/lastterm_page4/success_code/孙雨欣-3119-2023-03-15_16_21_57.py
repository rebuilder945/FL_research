ls1=eval(input())
a=len(ls1)
ls1.sort()
t=ls1[-1]
for i in range(a-1,-1,-1):
    if ls1[i]==t:
        del ls1[i]
    else:
        t=ls1[i]
print(ls1)
