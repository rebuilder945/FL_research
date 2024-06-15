a=input().split(",")
b=eval(input())
v=[]
for i in range(len(a)):
    h=[a[i],eval(b[i])]
    v.append(h)
print(v)
