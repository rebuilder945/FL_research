a=eval(input())
c=[]
for y in range(len(a)):
    c.append(int(a[y]))
for x in range(len(c)):
    c[x]=(c[x]+5)%10
c.reverse()
for i in range(len(c)):
    print(c[i],end='')

    


