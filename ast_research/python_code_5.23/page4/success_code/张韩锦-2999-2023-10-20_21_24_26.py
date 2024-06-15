lst=input().split(" ")
n,m=int(input())
del lst[n]
lst.insert(n,m)
del lst[m]
lst.insert(m,n)

