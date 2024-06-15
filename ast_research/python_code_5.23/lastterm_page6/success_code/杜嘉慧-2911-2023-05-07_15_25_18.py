s=input()
c=[]
for i in range(len(s)):
    c.append(int(s[i]))
for i in range(len(c)):
    c[i]=(c[i]+5)%10
c.reserve()
print(c)

