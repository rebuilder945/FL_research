a = list(range(int(input())))
for i in range(len(a)):
    a[i],a[i+1] = a[i+1],a[i]
print(a)


