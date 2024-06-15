list1 = list(map(str,input().split()))
n,m = map(int,input().split())
a = list1[n]
b = list1[m]
list1[n] = b
list1[m] = a
print(list1)


