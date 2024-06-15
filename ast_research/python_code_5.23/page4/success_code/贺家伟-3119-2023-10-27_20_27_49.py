a=eval(input())
b=[]
for i in range(len(a)-1,0,-1):
    if a[i] not in b:
        b.insert(0,a[i])
print(b)
