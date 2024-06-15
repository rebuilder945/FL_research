a=input()
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
for j in range(len(b)):
    c[j]=(c[j]+5)%10
c.reverse()
for k in range(len(c)):
               print(c[k],end="")

