n,m,l = eval(input())
lst = []
lst.append(n)
for i in range(m):
    lst.append(lst[-1] + l)
print(lst)

