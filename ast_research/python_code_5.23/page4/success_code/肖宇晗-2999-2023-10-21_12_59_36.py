l = input().split(",")
n,m = eval(input())
a = len(l)-1
for n,m in range(a):
    b = l[n]
    l[n] = l[m]
    l[m] = b
    print(l)
