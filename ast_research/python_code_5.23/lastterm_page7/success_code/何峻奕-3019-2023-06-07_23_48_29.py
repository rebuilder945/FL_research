s=input().split()
a=[]
for i in s[1:4]:
    a.append(round(int(i),2))
a.sort(reverse=True)
avg=round(sum(a)/3,2)
a.append(avg)
print([float(s[0])]+a)
