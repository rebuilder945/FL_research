n,m=map(int,input().split())
list1=[]
if n<=m-3 and n>0 and m>0:
    if n<=m-3 and n!=0:
        s=''
        for x in range(n,m):
            for y in range(n,m):
                for z in range(n,m):
                    if x!=y and x!=z and y!=z:
                        s=str(x)+str(y)+str(z)
                        if int(s) not in list1:
                            list1.append(int(s))
    elif n<=m-3 and n==0:
        s=''
        for x in range(n,m):
            for y in range(n,m):
                if x!=y:
                    s=str(x)+str(y)+str(0)
                    if int(s) not in list1:
                        list1.append(int(s))
    elif n<=m-3 and n==0:
        s=''
        for x in range(n,m):
            for y in range(n,m):
                if x!=y:
                    s=str(x)+str(0)+str(y)
                    if int(s) not in list1:
                        list1.append(int(s))
    list1.sort()
    print(*list1,sep=" ")
else:
    print("illegal input")
