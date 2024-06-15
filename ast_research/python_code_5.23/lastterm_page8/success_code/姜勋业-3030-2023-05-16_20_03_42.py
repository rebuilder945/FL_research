a=input().split(",")
b=input().split(",")
m=[]
for i in range(len(a)):
    k=[]
    k.append(a[i])
    k.append(int(b[i]))
    m.append(k)
b=sorted(m,key=lambda x:x[1])
print(b)
