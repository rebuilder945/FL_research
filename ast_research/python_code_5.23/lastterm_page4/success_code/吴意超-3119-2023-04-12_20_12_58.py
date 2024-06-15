a = eval(input())
b = []
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
b.reverse()
print(b)
