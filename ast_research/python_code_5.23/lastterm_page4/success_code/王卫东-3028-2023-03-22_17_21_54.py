n,m,l =eval(input())
a = [n]
for x in range(m-1):
    n = n+l
    a.append(n)
print(a)
