a=input().split(",")
b=eval(input())
y=[[a[i],b[i]]for i in range(len(a))]
y.sort(key=lambda x:x[1])
print(y)
