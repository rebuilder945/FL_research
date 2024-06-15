n,m=input().split()
n=int(n)
m=int(m)
ls1=[]
ls2=[]
if m<n or m-n<3 or m<0 or n<0 or n>8:
    print("illegal input")
else:
    for i in range(n,m):
        ls1.append(i)
    for x in range(len(ls1)):
        for y in range(len(ls1)):
            for z in range(len(ls1)):
                if x!=y and y!=z and x!=z and ls1[x]!=0:
                    a=str(ls1[x])+str(ls1[y])+str(ls1[z])
                    if a not in ls2:
                        ls2.append(a)
                    else:
                        continue
                else:
                    continue
    for i in ls2:
        i=int(i)
        print("%d"%i,end=' ')

