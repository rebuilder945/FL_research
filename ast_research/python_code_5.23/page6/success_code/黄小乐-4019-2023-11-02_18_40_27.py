a=input()
c=[]
for i in range (len(a)):
    c.append(int(a[i]))
for x in range(len(c)):
    c[x]=(c[x]+5)%10
c.reverse()
for k in range(len(c)):
    print(c[k],end="")







