a=input()
c=[]
for i in range(len(a)):
    c.append(int(a[i]))
for i in range(len(c)):
    c[i]=(c[i]+5)%10
c.reverse()
for x in range(len(c)):
    print(c[x],end="")


