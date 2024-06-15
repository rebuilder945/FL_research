#n  m
n,m=input().split(" ")
n=int(n)
m=int(m)
sum = []
sum1 = []
if(m<n) or (m-n)<3 or m<0 or n<0 or n>8:
    print("illegal input")
else:
    for x in range(n,m):
        sum.append(x)
    for x in range(len(sum)):
        for y in range(len(sum)):
            for z in range(len(sum)):
                if x!=y and y!=z and x!=z and sum[x]!=0:                   
                    s1=str(sum[x])+str(sum[y])+str(sum[z])
                    if s1 not in sum1:
                        sum1.append(s1)
                    else:
                        pass
                else:
                    pass
                   
    for y in sum1:
        y=int(y)
        print("%d "%y,end="")




