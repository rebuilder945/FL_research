list1 = input().split()
n,m = eval(input())
a = list1[n]
b = list1[m]
list1[m] = a
list1[n] = b
print(list1)
