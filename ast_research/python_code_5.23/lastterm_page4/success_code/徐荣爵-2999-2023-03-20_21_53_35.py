lst = list(input().split(' '))
lst2 = list(input().split(' '))
n = int(lst2[0])
m = int(lst2[1])
n = int(n)
m = int(m)
n1 = []
m1 = []
n1 = n1.append(lst[n])
m1 = m1.append(lst[m])
n2 = n1[0]
m2 = m1[0]
lst[m] = n2
lst[n] = m2
print(lst)
