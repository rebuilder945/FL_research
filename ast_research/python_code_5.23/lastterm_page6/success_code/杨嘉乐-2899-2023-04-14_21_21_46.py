import itertools as iter
l,r=map(int,input().split(" "))
pp=0
if 0<=r<10 and 0<=l<10 and r-l<3:
    pp=1
l=[x+l for x in range(r-l)]
ll=list(iter.permutations(l,3))
if pp==1:
    for i in ll:
        if i[0]!=0:
            print(*i,sep='',end=' ')
elif pp==0:
    print("illegal input")
