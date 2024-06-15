a=list(eval(input()))

for i in range(0,len(a)):
    if a.count(a[i])!=1:
        a.remove(a[i])
print(a)

