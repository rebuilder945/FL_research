n,m,l = eval(input())
a = []
for i in range(1,m+1):
    s = n + l*(i-1)
    i = i + 1
    a.append(s)
print(a)

