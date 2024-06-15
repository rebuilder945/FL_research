n,m=map(int,input().split())
if n<m-2 and isinstance(n,int)and n>0 and m>0 and n<10 and m<10:
    list1=[]
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    list1.append(x*100+y*10+z)
    for i in list1:
        print(i,end=" ")
else:
    print("illegal input")
