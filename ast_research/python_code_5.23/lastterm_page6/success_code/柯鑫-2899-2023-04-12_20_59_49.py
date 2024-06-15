n,m=map(int,input().split(""))
if n>0 and m>0 and m-n>=3 and n<10 and m<10:
    list1=[]
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    list1.append(100*x+10*y+z)
    for i in list1:
        print(i,end="")
elif n==0 and m>0 and m-n>=4 and n<10 and m<10:
    list1=[]
    for x in range(n+1,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    list1.append(100*x+10*y+z)
    for i in list1:
        print(i,end="")
else:
    print("illegal input")
