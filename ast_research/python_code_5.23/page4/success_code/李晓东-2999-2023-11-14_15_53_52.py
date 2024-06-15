list1 = list(map(str,input().split()))
n,m = eval(input())
a = list1[n]
b = list1[m]
list1[n] = b
list1[m] = a
print(list1)


