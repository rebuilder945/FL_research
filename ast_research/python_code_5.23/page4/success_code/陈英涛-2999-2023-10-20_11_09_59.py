l2 = input()
l1 = list(l2)
n,m = eval(input())
s = l1[n]
l1[n] = l1[m]
l1[m] = s
print(l1)

