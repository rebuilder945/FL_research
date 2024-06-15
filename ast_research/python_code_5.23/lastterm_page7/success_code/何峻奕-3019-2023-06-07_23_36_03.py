s=input().split()
a=[]
for i in s[1:4]:
    a.append("%.2f"%int(i))
a.sort(reverse=True)
avg="%.2f"%(sum(a)/3)
a.append(avg)
print([s[0]]+a)
