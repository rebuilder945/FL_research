a=eval(input())
m=[]
b=len(a)
for i in range(0,b):
    if a[i] not in m:
        m.append(a[i])
print(m)
