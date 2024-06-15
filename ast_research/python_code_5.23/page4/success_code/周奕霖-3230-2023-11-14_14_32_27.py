a = eval(input())
a.sort(reverse = True)
a = [str(i) for i in a]
for i in range(len(a)):
    b = sum(a[i])
print(b)


