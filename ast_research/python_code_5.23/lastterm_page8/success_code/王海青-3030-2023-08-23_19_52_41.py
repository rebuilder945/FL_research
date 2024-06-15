a=input().split(",")
b=eval(input())
b=b.sort()
v=[]
for i in range(len(a)):
    v.append([a[i],b[i]])
print(v)
