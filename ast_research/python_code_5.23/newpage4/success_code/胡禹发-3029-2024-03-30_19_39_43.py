a=list(input().split(","))
b=list(eval(input()))
c=[[1]]
for i in range(len(b)):
    d=[a[i],b[i]]
    c=c+[d]
c.remove([1])
print(c)
