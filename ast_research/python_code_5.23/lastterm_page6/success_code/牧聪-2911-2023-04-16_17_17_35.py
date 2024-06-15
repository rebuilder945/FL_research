a=int(input())
aa=str(a)
aa=aa.split()
b=[]
for x in a:
    t=(int(x)+5)%10
    b.append(t)
b.reverse()
b="".join(str(i) for i in b)

