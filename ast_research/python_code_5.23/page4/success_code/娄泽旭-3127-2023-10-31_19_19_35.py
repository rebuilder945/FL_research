x = eval(input())
b = []
a = [i+1 for i in range(x)]
for c in range(1,x):
    b.append(a[c])
b.append(a[0])
print(b)
