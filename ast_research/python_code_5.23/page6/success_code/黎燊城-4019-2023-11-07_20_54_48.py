a=input()
c=[]
for i in range(len(a)):
    c.append((int(a[i])+5)%10)
c.reverse()
for k in range(len(c)):
    print(c[k], end='')
