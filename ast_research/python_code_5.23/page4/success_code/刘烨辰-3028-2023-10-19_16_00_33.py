n,m,l = eval(input())
list1 = []
list1.append(n)
for i in range(m-1):
    n = n + l
    list1.append(n)
print(list1)
