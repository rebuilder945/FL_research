def ss(n):
    for i in range(2,n):
        t=n%i
        if t==0:
            break
    else:
        return 1
ii=[]
lt=eval(input())
for i in lt:
    if ss(i) and i!=0 and i!=1:
        ii.append(i)
print(ii)

