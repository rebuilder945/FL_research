a=eval(input())
a.sort(reverse=True)
b=""
for x in range(len(a)):
    b.append(a[x])
print(b)
