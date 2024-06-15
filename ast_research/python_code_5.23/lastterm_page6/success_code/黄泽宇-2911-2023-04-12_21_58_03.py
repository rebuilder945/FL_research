a=input()
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
for x in range(len(b)):
    b[x]=(b[x]+5)%10
c=b[::-1]
for k in range(len(c)):
    print(c[k],end='')

