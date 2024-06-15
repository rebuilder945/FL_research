a=(input()).split(",")
b=eval(input())
c=[[a[i]]+[b[i]]for i in range(len(a))]
print(c)
