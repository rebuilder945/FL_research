a=input().split(",")
b=input().split(",")
v=[]
for i in range(len(a)):
    h=[a[i],eval(b[i])]
    v.append(h)
print(v)
