a = eval(input())
a.sort(reverse=True)
b = 0
for x in range(len(a)):
    b+=str(a[x])
print(int(b))

