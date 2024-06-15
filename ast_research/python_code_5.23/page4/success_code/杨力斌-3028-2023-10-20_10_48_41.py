n,m,l = eval(input())
lst = [n]
for i in range(m-1):
    n = n + l
    lst.append(n)
print(lst)
