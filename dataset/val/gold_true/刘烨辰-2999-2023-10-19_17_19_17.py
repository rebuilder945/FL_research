list1 = input().split()
n,m = input().split()
a = list1[int(n)]
b = list1[int(m)]
list1[int(m)] = a
list1[int(n)] = b
print(list1)
