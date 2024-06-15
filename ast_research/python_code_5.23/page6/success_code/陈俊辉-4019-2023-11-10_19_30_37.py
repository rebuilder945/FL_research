a=input()
b=[]
for i in range(len(a)):
    b.append (int(a[i]))
for j in range(len(b)):
    b[j]=(b[j]+5)%10
b.reverse()
for k in range(len(b)):
    print(b[k],end='')


