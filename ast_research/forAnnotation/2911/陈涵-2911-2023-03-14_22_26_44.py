a=input("")
s=[(int(a[i])+5)% 10 for i in range(len(a))]
s2=[s[i]*10**i for i in range(len(s))]
print(sum(s2))

