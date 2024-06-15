from platform import release
ls1=list(input())
for i in range(len(ls1)):
    ls1[i]=(eval(ls1[i])+5)%10
ls1[0],ls1[-1],ls1[1],ls1[-2]=ls1[-1],ls1[0],ls1[-2],ls1[1],
for i in ls1:
    print(i,end="")
