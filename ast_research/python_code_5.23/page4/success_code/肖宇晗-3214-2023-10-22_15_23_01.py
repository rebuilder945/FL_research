l = eval(input())
n = len(l)
for i in range(n):
    for j in range(n-1):
        if l[j]==0:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

