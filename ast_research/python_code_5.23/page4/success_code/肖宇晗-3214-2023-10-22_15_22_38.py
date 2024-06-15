l = eval(input())
n = len(l)
for i in range(n):
    for j in range(n-1):
        if l[i]==0:
            l[i],l[i+1]=l[i+1],l[i]
print(l)

