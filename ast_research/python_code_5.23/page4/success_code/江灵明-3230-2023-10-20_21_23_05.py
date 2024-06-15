a = eval(input())
a.sort(reverse=True)
b = ""
for x in range(len(a)):
    b+=a[x]
print(int(b))

