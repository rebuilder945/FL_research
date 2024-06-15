a=input().split(",")
b=eval(input())
v=[]
for i in range(len(a)):
    v.append([a[i],eval(b[i])])
print(v)
