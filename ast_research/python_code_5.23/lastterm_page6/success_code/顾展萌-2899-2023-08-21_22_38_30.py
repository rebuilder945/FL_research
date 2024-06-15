n,m=input().split(" ")
n = int(n)
m = int(m)
sum = []
sum1 = []
if n >= m or n<0 or m<0:
    print("illegal input")
elif (m - n) <3:
    print("illegal input")
else:
    for i in range(n,m):
        sum.append(i)
    for x in range(len(sum)):
        for y in range(len(sum)):
            for z in range(len(sum)):
                if x!=y and y!=z and x!=z:
                    s1 = str(sum[x])+str(sum[y])+str(sum[z])
                    if s1 not in sum1:
                        sum1.append(s1)
                    else:
                        pass
                else:
                    pass
for i in sum1:
    y = int(y)
    print(i,end='')



