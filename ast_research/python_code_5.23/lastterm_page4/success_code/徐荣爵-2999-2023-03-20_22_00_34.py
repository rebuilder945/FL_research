lst = list(input().split(' '))
lst2 = list(input().split(' '))
n = int(lst2[0])
m = int(lst2[1])
n = int(n)
m = int(m)
n1 = lst[n]
lst[n] = lst[m]
lst[m] = n1
print(lst)
