import itertools as iter
l,r=map(int,input().split(" "))
pp=1
if type(r)!=int or type(l)!=int or r<0 or l<0 or r-l<3 or r>10:
    pp=0
l=[x+l for x in range(r-l)]
ll=list(iter.permutations(l,3))
if pp==1:
    for i in ll:
        if i[0]!=0:
            print(*i,sep='',end=' ')
elif pp==0:
    print("illegal input")
