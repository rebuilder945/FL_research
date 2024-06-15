#判断是否不重复数字
def chachong(n):
    a=1
    m=str(n)
    for x in m:
        if m.count()!=1:
            a=0
            break
    return a
p=input()
l=p.split(" ")
n=l[0]
m=l[1]
sum=[]
sum1=[]
if n>=m or m-n<3 or n>8:
    print("illegal input")
else:
    for i in range(n,m):
        sum.append(i)
    for x in range(len(sum)):
        for y in range(len(sum)):
            for z in range(len(sum)):
                if x!=0 and x!=y and x!=z and y!=z:
                    s=sum[x]+sum[y]+sum[z]
                    sum1.append(s)
print(" ".join(sum1))
