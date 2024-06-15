n, m, l = eval(input())
lst = [n]
for i in range(m-1):
    n += l
    lst.append(n)
print(lst)
