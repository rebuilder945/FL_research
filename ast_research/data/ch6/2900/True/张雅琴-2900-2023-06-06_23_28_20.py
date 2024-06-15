a=eval(input())
b=[]
c=[]
if a-int(a)!=0 or a<=1:
    print("illegal input")
else:
    for i in range(2,a+1):
        d=[str(i)[x] for x in range(0,len(str(i)))]
        e=d.copy()
        d.reverse()
        if d==e:
            b.append(i)
    for i in range(2,a+1):
        f=0
        for j in range(2,i):
            if i%j==0:
                f+=1
        if f==0:
            c.append(i)
for i in b:
    if i in c:
        print(i,end=" ")



