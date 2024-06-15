a=int(input())
aa=str(a)
aa=aa.split()
b=[]
for x in aa:
    t=(x+5)%10
    b.append(t)
b.reverse()
b="".join(str(i) for i in b)

