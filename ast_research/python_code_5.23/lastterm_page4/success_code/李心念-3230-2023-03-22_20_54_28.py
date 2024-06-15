a = eval(input())
a.sort(reverse=True)
b = []
for i in range(len(a)):
    b1 = str(a[i])
    b.append(b1)
for i in range(len(a)):
    print(b[i],end="")
