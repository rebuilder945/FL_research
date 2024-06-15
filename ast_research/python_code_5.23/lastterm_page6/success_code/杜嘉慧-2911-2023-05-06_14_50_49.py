a=input()
c=[]
for i in range(len(a)):
    c[i]=(c[i]+5)%10
c.reverse()
for j in range(len(c)):
    print(c[j],end='')


