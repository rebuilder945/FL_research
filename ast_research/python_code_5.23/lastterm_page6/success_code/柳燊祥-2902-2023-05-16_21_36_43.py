n=int(input())
fz=[2,3]
fm=[1,2]
sum=0
if n<2:
    for i in range(n):
        sum+=fz[i]/fm[i]
else:
    for i in range(2,n):
        a=fz[i-1]+fm[i-1]
        b=fz[i-2]+fm[i-2]
        fz.append(a)
        fm.append(b)
        for i in range(n):
            sum+=fz[i]/fm[i]
print("%.4f"%sum)
