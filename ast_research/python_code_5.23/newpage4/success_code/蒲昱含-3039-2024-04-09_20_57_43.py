a=int(input())
b=[]
for i in range(len(a)):
    for t in range(len(a)):
        for p in range(len(a)):
            if a[i]<=a[:len(a)]:
                a[t]>a[i]
                if a[p]>=a[:len(a)]:
                    a[t]<a[p]
                    b.append(a[t])
print(b)
