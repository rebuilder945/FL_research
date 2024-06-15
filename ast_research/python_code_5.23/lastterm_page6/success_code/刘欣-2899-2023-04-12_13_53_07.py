
n,m=input().split(" ")
n=int(n)
m=int(m)
lis1=[]
lis2=[]
if m-n<3 or m<n or n!=int(n) or m!=int(m) or n<0 or m>9:
    print("illegal input")
else:
    for i in range(n,m):
        lis1.append(i)
    for x in lis1:
        for y in lis1:
            for z in lis1:
                if x!=y and x!=z and y!=z and x!=0:
                    shu=str(x)+str(y)+str(z)
                    if shu not in lis2:
                        lis2.append(shu)
                    else:
                        pass
                else:
                     pass
    for i in lis2:
        print("%s"%i,end=" ")
