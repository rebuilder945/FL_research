a = eval(input())
n,m = eval(input())
i = a.index(n)
d = a.index(m)
l[i],l[d] = l[d],l[i]
print(a)
