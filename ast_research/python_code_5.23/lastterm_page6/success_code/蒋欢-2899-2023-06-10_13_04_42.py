p=input()
l=p.split(" ")
n=int(l[0])
m=int(l[1])
sum=[]
sum1=[]
if n>=m or m-n<3 or n>8 or n<0 or m<0:
    print("illegal input")
else:
    for i in range(n,m):
        sum.append(str(i))
    for x in range(len(sum)):
        for y in range(len(sum)):
            for z in range(len(sum)):
                if sum[x]!="0" and x!=y and x!=z and y!=z:
                    s=sum[x]+sum[y]+sum[z]
                    if s not in sum:
                        sum1.append(s)
print(" ".join(sum1))
