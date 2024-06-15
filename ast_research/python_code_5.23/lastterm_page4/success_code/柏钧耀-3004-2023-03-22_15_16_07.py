a=eval(input())
n=max(a)
for i in a[2:n]:
    for j in range(2,n):
        if i%j==0:
            a.remove(i)
        else:
            pass
print(a)

