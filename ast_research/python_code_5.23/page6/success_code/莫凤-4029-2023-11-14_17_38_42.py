n,m=map(int,input().split())
list1=[]
if n<=m-3 and n>0 and m>0:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    a=int(str(x)+str(y)+str(z))
                    if a>99:
                        list1.append(a)
    if len(list1)==0:
        print("illegal input")
    else:
        print(*list1,sep=" ")
else:
    print("illegal input")
