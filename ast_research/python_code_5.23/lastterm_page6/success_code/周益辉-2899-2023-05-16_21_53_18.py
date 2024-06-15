n,m=map(int,input().split(" "))
if n>0 and m>0 and m-n>=3 and n<10 and m<10:
    lst1=[]
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    lst1.append(x*100+y*10+z)
    for i in lst1:
        print(i,end=" ")
elif n==0 and m>0 and m-n>=4 and n<10 and m<10:
    lst1=[]
    for x in range(n+1,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    lst1.append(x*100+y*10+z)
    for i in lst1:
        print(i,end=" ")
else:
    print("illegal input")


