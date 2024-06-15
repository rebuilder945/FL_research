a=eval(input())
a.sort(reverse=True)
b=""
for x in range(len(a)):
    b.append(str(a[x]))
print(int(b))
