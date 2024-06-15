a = eval(input())
a.sort(reverse = True)
a = [str(i) for i in a]
for x in range(len(a)):
    b = sum(a[x])
print(b)


