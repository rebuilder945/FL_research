c=list(input())
for i in range(len(c)):
    c[i]=(eval(c[i])+5)%10
c[0],c[-1],c[1],c[-2]=c[-1],c[0],c[-2],c[1]
for i in c:
    print(i,end='')
print(c)
