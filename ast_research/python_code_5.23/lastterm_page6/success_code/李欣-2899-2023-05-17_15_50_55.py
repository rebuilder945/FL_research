n,m=map(int,input().split(" "))
if n>0 and m>0 and m-n>=3 and n<10 and m<10:
    ls1=[]
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and y!=z and x!=z:
                    ls1.append(x*100+y*10+z)
    for i in ls1:
        print(i,end=" ")
elif n==0 and m>0 and m-n>=3 and m<10:
    ls1=[]
    for x in range(1,m):
        for y in range(1,m):
            for z in range(1,m):
                if x!=y and y!=z and x!=z:
                    ls1.append(x*100+y*10)
                    ls1.append(x*100+y)
                    ls1.append(x*100+y*10+z)
                    ls1.sort()
    for i in ls1:
        print(i,end=" ")
else:
    print("illegal input")
