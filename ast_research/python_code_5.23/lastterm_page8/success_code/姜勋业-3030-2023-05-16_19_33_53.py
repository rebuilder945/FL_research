a=input().split(",")
b=input().split(",")
m=[]
for i in range(len(a)):
    k=[]
    k.append(a[i])
    k.append(int(b[i]))
    m.append(k)
print(m)
