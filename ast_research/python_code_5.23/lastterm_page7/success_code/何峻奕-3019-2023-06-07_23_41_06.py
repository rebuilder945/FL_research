s=input().split()
a=[]
for i in s[1:4]:
    a.append(int(i))
a.sort(reverse=True)
avg=(sum(a)/3)
a.append(avg)
print([eval(s[0])]+a)
