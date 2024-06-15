a=input()
c=[]
for i in range(len(a)):
    c.append(int(a[i]))
for x in range(len(c)):
    c[x]=(c[x]+5)%10
c.reverse()
for y in range(len(c)):
    print(c[y],end='')
