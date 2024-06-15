a = eval(input())
for i in range(len(a)):
    if a[i] ==0:
        del a[i]
        a.append(0)
print(a)

