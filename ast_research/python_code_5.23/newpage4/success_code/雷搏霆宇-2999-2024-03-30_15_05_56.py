a = input().split()
n,m = map(int,input().split())
# a = list(eval(input()))
# m,n = eval(input())
a[n],a[m] = a[m],a[n]
print(a)

