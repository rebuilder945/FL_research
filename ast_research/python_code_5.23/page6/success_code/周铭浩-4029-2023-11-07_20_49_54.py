n,m=input().split(" ")
n=int(n)
m=int(m)
sum=[]
sum2=[]
if n>=m or m-n<3 or n<0 or n>=8:
    print('illegal input')
else:
    for x in range (n,m):
        sum.append(x)
    for x in range(len(sum)):
        for y in range(len(sum)):
            for z in range(len(sum)):
                if x!=y and x!=z and y!=z :
                    s1=str(sum[x])+str(sum[y])+str(sum[z])
                    if s1 not in sum2:
                        sum2.append(s1)
                    else:
                        pass
                else:
                    pass
    for y in sum2:
        y=int(y)
        print('%d'%y,end=" ")

